from transformers import LlamaForCausalLM, AutoConfig, AutoTokenizer, LlamaTokenizer
from tool import sum_parameters

if __name__ == '__main__':
    model_path = './model_file/LLaMA-zh-base/'
    config = AutoConfig.from_pretrained(model_path)
    model = LlamaForCausalLM(config)
    model.half()
    sum_parameters(model)
    model.save_pretrained(model_path)
    print('init model over')
