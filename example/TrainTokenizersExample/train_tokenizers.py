# coding=utf-8
import tokenizers
from datasets import load_dataset
from tokenizers.normalizers import NFD, StripAccents
from tokenizers.pre_tokenizers import Digits, ByteLevel, Punctuation, Whitespace, CharDelimiterSplit, UnicodeScripts, \
    Metaspace
from tokenizers.trainers import BpeTrainer
from tokenizers import Tokenizer, normalizers, pre_tokenizers, decoders
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE())
normalizer = normalizers.Sequence([NFD(), StripAccents()])
tokenizer.normalizer = normalizer
# 我们主要使用四类分割，空白，标点符号，数字，及Bytelevel
tokenizer.pre_tokenizer = pre_tokenizers.Sequence(
    [Whitespace(), Punctuation(), Digits(individual_digits=True), UnicodeScripts(), ByteLevel(use_regex=False)])
# 需要设置解码器为BPE
tokenizer.decoder = decoders.ByteLevel(add_prefix_space=True, use_regex=False)
# 字节级 BPE 可能在生成的令牌中包括空白。如果您不希望偏移量包含这些空格，那么必须使用这个 PostProcessor。
tokenizer.post_processor = tokenizers.processors.ByteLevel()
special_tokens = ["[PAD]", "<s>", "</s>"]

r = tokenizer.add_special_tokens(special_tokens)
tokenizer.enable_padding()

dataset = load_dataset('text', data_files={'train_file': "./train_data.csv"}, cache_dir='./cache/')

def batch_iterator(batch_size=10000):
    for i in range(0, len(dataset['train_file']), batch_size):
        yield dataset['train_file'][i: i + batch_size]["text"]

trainer = BpeTrainer(vocab_size=45999, special_tokens=special_tokens)
tokenizer.train_from_iterator(batch_iterator(), trainer=trainer, length=len(dataset['train_file']))
tokenizer.save("./output/BPE_tokenizer.json")
