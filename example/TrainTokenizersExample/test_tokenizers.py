from transformers import AutoTokenizer,LlamaTokenizerFast
model_path = "./output/"
tokenizer = LlamaTokenizerFast(tokenizer_file="./output/BPE_tokenizer.json",pad_token="[PAD]",)
print(tokenizer)


tokenizer.save_pretrained('./output/llama/')

tokenizer = LlamaTokenizerFast.from_pretrained('./output/llama/')

print(len(tokenizer))
print(tokenizer)
tokenizer.save_pretrained('./output/llama/')
print('tokenize')
content = '白日依山尽，黄河入海流.欲穷千里目,更上一层楼。'
r = tokenizer.tokenize(content)
print(tokenizer)
print(len(content), len(r))
print(r)

content = '太太好啊，世界。我啊'
r = tokenizer.tokenize(content)
ids = tokenizer.encode(content)
texts = [tokenizer.convert_tokens_to_string([m]) for m in r]
print(texts)
print(tokenizer)
print(ids)
print(len(content), len(r),len(ids))
print(r)

r = tokenizer.decode(tokenizer.encode_plus(content)['input_ids'],clean_up_tokenization_spaces=True)
print(r)

content = '<s> </s> Cảm ơn Hẹn gặp bạn sau'
r = tokenizer.tokenize(content)
print(r)
r = tokenizer.decode(tokenizer.encode_plus(content)['input_ids'],clean_up_tokenization_spaces=True)
print(r)

print(tokenizer)
print(len(tokenizer))
