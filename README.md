# Chatterbox

Read this in [English](./README_EN.md).

<div align="left">
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/LianjiaTech/BELLE/blob/main/LICENSE)
[![Model License](https://img.shields.io/badge/Model%20License-GPL_v3.0-green.svg)]()
![GitHub last commit](https://img.shields.io/github/last-commit/enze5088/Chatterbox)
<a href="https://github.com/enze5088/Chatterbox/stargazers">![GitHub Repo stars](https://img.shields.io/github/stars/enze5088/Chatterbox)</a>
</div>

本项目持续收集整理并分享关于大语言模型的相关内容，主要包括以下三类：

1. 持续收集整理并分享关于大语言模型的相关中文数据集：如预训练数据集、指令微调数据集、
2. 提供中文对话模型 、中文基础模型及预训练框架构建。陆续开放不同规模的中文基础模型权重
3. 分享基于中文大语言模型的相关应用及代码等。

### 包含内容

1. 中文NLP相关的可用的数据集，分享开源与发布新爬取的数据集。详细介绍[见此](./docs/datasets.md)
2. 中文基础模型分享
   1. 基于BloomZ 1B2 的中文语言模型。裁剪词表和WordsEmbedding后参数量为0.9B左右，使用开源指令数据进行微调训练。目前主要使用Belle,alpaca_gpt4_data_zh,firefly 微调。
   2. 从头预训练中文LLaMA模型。
      1. [Chatterbox-LLaMA-zh-base](https://huggingface.co/TurboPascal/Chatterbox-LLaMA-zh-base) 使用33G语料从头预训练初始化的LLaMA-base中文模型，重新制作了中文词表与分词器。详细介绍见[该文档](./docs/model/llama-zh-base)
3. 语言模型的相关应用
   1. 基于大模型的Web聊天Demo与微信机器人实现。


## 数据集
整理并当前可用的中文NLP相关的大模型训练的数据集，目前已整理30+。并陆续发布新爬取的中文数据集。

详细数据集收集与整理见此[介绍](./docs/datasets.md)

### 开源数据集

本项目爬取并整理的部分数据。

- [人民日报数据集](https://pan.baidu.com/s/1g47vdWwGjAXleEYR0GcfSg?pwd=l6q8) ：194603月-201012月 其中2004-2010年数据集缺失标题并有格式混乱的现象。
- 新浪新闻数据集：

## 模型

### Chatterbox-LLaMA-zh-base

[huggingface链接](https://huggingface.co/TurboPascal/Chatterbox-LLaMA-zh-base)

使用33G中文语料重头开始预训练的Llama-base模型，参数量约为0.8B左右。旨在提供可用的中小型基础模型。针对中文语料重新构建了embedding层和tokenizer。未经过指令微调。无需遵守原LLaMA权重协议。

## License

The use of this repo is subject to the [Apache License](https://github.com/enze5088/Chatterbox/blob/main/LICENSE)
