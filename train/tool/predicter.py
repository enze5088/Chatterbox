from optimum.bettertransformer import BetterTransformer
from transformers import BloomForCausalLM, AutoTokenizer

class Predicter:
    def __init__(self,model_path,device='cuda', max_length=768):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = BloomForCausalLM.from_pretrained(model_path)
        # self.model = BetterTransformer.transform(self.model, keep_original_model=True)
        self.device = device
        self.model.to(device).eval()
        self.max_length = max_length

    def __call__(self, text,
                 num_beams=2, num_return_sequences=1,
                 temperature=1, top_p=1,top_k=50,
                 do_sample=False, early_stopping=True,no_repeat_ngram_size=2,
                 **kwargs):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, return_token_type_ids=False,
                                max_length=self.max_length, truncation=True)
        inputs.to(self.device)
        outputs = self.model.generate(**inputs,
                                      num_return_sequences=num_return_sequences,
                                      max_length=self.max_length,
                                      # top_k=top_k,
                                      # top_p=top_p,
                                      # no_repeat_ngram_size=no_repeat_ngram_size,
                                      temperature=temperature,
                                      num_beams=num_beams,
                                      do_sample=do_sample,
                                      early_stopping=early_stopping)
        text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True,
                                           clean_up_tokenization_spaces=True)
        text = [item.replace(' ', '') for item in text]
        return text