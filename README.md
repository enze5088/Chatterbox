# Chatterbox
基于BloomZ1B2 的中文语言模型。裁剪词表和WordsEmbedding后参数量为0.9B左右。使用以下开源数据进行训练。

目前主要使用Belle,alpaca_gpt4_data_zh,firefly 微调。

A Chinese Language Model base on BloomZ1B.


### Datasets
#### Insturct Data
- [Belle](https://huggingface.co/BelleGroup)
- [alpaca_gpt4_data_zh](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM/blob/main/data/alpaca_gpt4_data_zh.json)
- [firefly](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M)

#### STS

- [LCQMC](https://aistudio.baidu.com/aistudio/competition/detail/45/0/task-definition)
- BQ CorpusBank Question Corpus
- PAWS-X (中文) 

#### QA

1. [cMedQA](https://github.com/zhangsheng93/cMedQA)
2. [cMedQA-2](https://github.com/zhangsheng93/cMedQA2)
3. [webMedQA](https://github.com/hejunqing/webMedQA)



## License

The use of this repo is subject to the [Apache License](https://github.com/enze5088/Chatterbox/blob/main/LICENSE)
