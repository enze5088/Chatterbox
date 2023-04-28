import tokenizers
from datasets import load_dataset
from tokenizers.normalizers import NFD, StripAccents
from tokenizers.pre_tokenizers import Digits, ByteLevel, Punctuation, Whitespace, CharDelimiterSplit
from tokenizers.trainers import BpeTrainer
from tokenizers import Tokenizer, normalizers, pre_tokenizers, decoders
from tokenizers.models import BPE


tokenizer = Tokenizer(BPE())
normalizer = normalizers.Sequence([NFD(), StripAccents()])
tokenizer.normalizer = normalizer
# 我们主要使用四类分割，空白，标点符号，数字，及Bytelevel
tokenizer.pre_tokenizer = pre_tokenizers.Sequence([Whitespace(), Punctuation(), Digits(individual_digits=True), ByteLevel()])
# 需要设置解码器为BPE
tokenizer.decoder = decoders.ByteLevel(add_prefix_space=True, use_regex=True)
# 字节级 BPE 可能在生成的令牌中包括空白。如果您不希望偏移量包含这些空格，那么必须使用这个 PostProcessor。
tokenizer.post_processor = tokenizers.processors.ByteLevel()

dataset = load_dataset("TurboPascal/tokenizers_example_zh_en", cache_dir='./cache/')


def batch_iterator(batch_size=10000):
    for i in range(0, len(dataset['train']), batch_size):
        yield dataset['train'][i: i + batch_size]["text"]

special_tokens = ["[CLS]", "[SEP]", "[PAD]", "[MASK]", "<s>", "</s>", "<t>", "</t>"]
trainer = BpeTrainer(special_tokens=special_tokens, vocab_size=54000)
tokenizer.train_from_iterator(batch_iterator(), trainer=trainer, length=len(dataset['train']))
tokenizer.save("./BPE_tokenizer.json")
