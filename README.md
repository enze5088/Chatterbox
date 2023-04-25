# Chatterbox
Read this in [English](./README_EN.md).

<div align="left">

<a href="https://github.com/enze5088/Chatterbox/stargazers">![GitHub Repo stars](https://img.shields.io/github/stars/enze5088/Chatterbox)</a>
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/LianjiaTech/BELLE/blob/main/LICENSE)

</div>

本项目将持续收集整理并分享关于大语言模型的相关内容：如预训练数据集、指令微调数据集、开源模型、应用等。

目前包括

1. 收集和整理中文NLP相关的可用的数据集，分享开源与发布新爬取的数据集。详细介绍[见此](./docs/datasets.md)
2. 基于BloomZ 1B2 的中文语言模型。裁剪词表和WordsEmbedding后参数量为0.9B左右，使用开源指令数据进行微调训练。目前主要使用Belle,alpaca_gpt4_data_zh,firefly 微调。
3. 从头预训练中文LLaMA模型。
4. 基于大模型的Web聊天Demo与微信机器人实现。

## 数据集
整理当前可用与大模型训练的数据集，目前已整理30+。详细数据集收集与整理见此[介绍](./docs/datasets.md)
### 开源数据集
本项目爬取并整理的部分数据。

- [人民日报数据集](https://pan.baidu.com/s/1g47vdWwGjAXleEYR0GcfSg?pwd=l6q8) ：194603月-201012月 其中2004-2010年数据集缺失标题并有格式混乱的现象。


## License

The use of this repo is subject to the [Apache License](https://github.com/enze5088/Chatterbox/blob/main/LICENSE)
