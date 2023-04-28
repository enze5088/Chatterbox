# 从头训练一个自己的Tokenizer
就当下而言，预训练语言模型对如今的NLP算法工程师已经非常常见了。基本上绝大多数的模型都需要使用到分词器（Tokenizer）。而大多数时候我们是去加载别人已经构建好的分词器。今天我们来尝试一下自己从头训练并构建自己的分词器。
一般而言，我们构建分词器可以通过sentencepiece或者huggingface的tokenizers框架来构建。今天我们选择使用tokenizers框架来实现训练自己的分词器。
首先是安装好自己的分词器框架，一般使用transformers框架的朋友都已经安装过了。这一部分可以忽略不计。
pip install tokenizers
然后我们需要添加好一个tokenizers基类，并为其设置各种类型的组件。在构建 Tokenizer 时，您可以将各种类型的组件附加到此 Tokenizer 以自定义其行为，大体上分为以下几个组件：
Models：模型是用于实际标记化的核心算法，因此，它们是tokenizer的唯一强制性组件。目前支持WordLevel，BPE，WordPiece，Unigram
Normalizers：Normalizer（规范化器） 负责预处理输入字符串，以便将其归一化为与给定用例相关的字符串。规范化的一些常见示例是 Unicode 规范化算法（NFD、NFKD、NFC 和 NFKC）、小写等……tokenizers的特殊性在于，我们在标准化的同时跟踪对齐。这对于允许从生成的标记映射回输入文本至关重要。
Pretokenizer：PreTokenizer(预分词器) 负责根据一组规则分割输入。这种预处理可以确保底层模型不会跨多个“拆分”构建令牌。例如，如果你不想在令牌中使用空格，那么你可以使用 PreTokenizer 分割这些空格。你可以使用一个序列轻松地将多个 PreTokenizer 组合在一起。PreTokenizer 也可以像 Normalizer 一样修改字符串。这对于允许一些复杂的算法在标准化之前需要进行分割是必要的(例如 ByteLevel)
PostProcessor：在完成整个流程之后，有时候我们希望在向模型(如“[ CLS ] My horse is magic [ SEP ]”)提供标记化字符串之前插入一些特殊的标记。PostProcessor 就是这样做的组件。 
Decoder：Decoder（解码器）知道如何从分词器(tokenizer)使用的 ID 返回到可读的文本。例如，某些Normalizers和Pretokenizer使用需要还原的特殊字符或标识符。
```
tokenizer = Tokenizer(BPE())
normalizer = normalizers.Sequence([NFD(), StripAccents()])
tokenizer.normalizer = normalizer
# 我们主要使用四类分割，空白，标点符号，数字，及Bytelevel
tokenizer.pre_tokenizer = pre_tokenizers.Sequence(
    [Whitespace(), Punctuation(), Digits(individual_digits=True), ByteLevel()])

tokenizer.decoder = decoders.ByteLevel(add_prefix_space=True, use_regex=True)
# 字节级 BPE 可能在生成的令牌中包括空白。如果您不希望偏移量包含这些空格，那么必须使用这个 PostProcessor。
tokenizer.post_processor = tokenizers.processors.ByteLevel()
```
这里我们使用ByteLevel BPE。主要优点是：
较小的词汇表
没有未知令牌
字节级 BPE 将所有 Unicode 代码点转换为多个字节级字符：
每个 Unicode 代码点被分解为字节（ASCII 字符为 1 个字节，UTF-8 Unicode 代码点最多为 4 个字节）
每个字节值都从 Unicode 表的开头获得一个分配给它的“可见”字符。这一点尤其重要，因为有很多控制字符，所以我们不能只有一个简单的映射 ASCII 表字符 <-> 字节值。所以一些字符得到其他表示，例如空白U+0020变成Ġ.
这样做的目的是，我们最终会得到一个包含 256 个标记的初始字母表。然后可以将这 256 个标记合并在一起以表示词汇表中的任何其他标记。这导致更小的词汇表，永远不需要“未知”标记。
```
dataset = load_dataset("TurboPascal/tokenizers_example_zh_en", cache_dir='./cache/')
print(dataset)
def batch_iterator(batch_size=10000):
    for i in range(0, len(dataset), batch_size):
        yield dataset['train'][i: i + batch_size]["text"]

special_tokens = ["[CLS]", "[SEP]", "[PAD]", "[MASK]", "<s>", "</s>", "<t>", "</t>"]
trainer = BpeTrainer(special_tokens=special_tokens, vocab_size=54000)
tokenizer.train_from_iterator(batch_iterator(), trainer=trainer, length=len(dataset['train']))

tokenizer.save("./BPE_tokenizer.json")
```

这里从dataset上拉取预先已经收集好的训练数据，并进行训练。