from transformers import AutoTokenizer, LlamaTokenizerFast
model_path = "./output/"
tokenizer = LlamaTokenizerFast(tokenizer_file="./BPE_tokenizer.json")
tokenizer.save_pretrained('./llama/')
tokenizer = LlamaTokenizerFast.from_pretrained('./llama/')
print(len(tokenizer))
print(tokenizer)
content = '白日依山尽，黄河入海流.欲穷千里目,更上一层楼。'
r = tokenizer.tokenize(content)
print(r)
r = tokenizer.decode(tokenizer.encode_plus(content)['input_ids'],clean_up_tokenization_spaces=True)
print(r)
