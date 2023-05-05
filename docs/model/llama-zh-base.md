# LLama-zh

欢迎来到本开源项目Chatterbox-Llama-zh

## 简介
LLama-zh-base模型是基于目前llama系列的模型架构，从头重新预训练的LLama模型。
由于llama原模型本身并未在中文语料上单独训练，词表中也并未包括太多的中文字符。
本项目重新构建了Llama的分词工具与词表。并重新初始化了对应的模型，在中文领域上的持续预训练。

## 模型内容

Chatterbox-Llama-zh系列

| 模型名称                 | 模型大小 | 链接                                                        |
| ------------------------ | -------- | ----------------------------------------------------------- |
| Chatterbox-Llama-zh-base | 0.8B     | https://huggingface.co/TurboPascal/Chatterbox-LLaMA-zh-base |
| Chatterbox-Llama-zh-2b6  | 2B6      | Coming soon                                                 |
|                          |          |                                                             |

Notes:

1. 本模型没有使用原LLaMA的权重，因此无需顾虑LLama权重协议的问题。

## 数据

预训练阶段使用开源数据与本项目爬取的部分数据。共使用约33G中文预训练数据

### 中文预训练数据

- 新浪新闻数据（SinaNews），220万条新闻文档数据
- 人民日报数据（People's Daily Datasets），
- [维基百科(wiki2019zh)，100万个结构良好的中文词条](https://github.com/brightmart/nlp_chinese_corpus)
- [新闻语料(news2016zh)，250万篇新闻，含关键词、描述](https://github.com/brightmart/nlp_chinese_corpus)
- [社区问答json版(webtext2019zh)，410万个高质量社区问答](https://github.com/brightmart/nlp_chinese_corpus)
- [THUCNews数据(THUCNews) ，74万篇新闻文档（2.19 GB）](http://thuctc.thunlp.org/#%E4%B8%AD%E6%96%87%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB%E6%95%B0%E6%8D%AE%E9%9B%86THUCNews)
- [评论数据-语料 （comments2019zh_corpus），240万条评论数据](https://github.com/CLUEbenchmark/CLUECorpus2020)
- [社区互动-语料 （webText2019zh_corpus），310W条社区互动数据](https://github.com/CLUEbenchmark/CLUECorpus2020)
- [科学文献数据（CSL）,  约40W篇中文核心期刊文献摘要](https://github.com/ydli-ai/CSL)
- [Belle数据集](https://huggingface.co/datasets/BelleGroup/train_2M_CN)

## 训练框架

见本项目Chatterbox代码

## 测试评估

待完成



## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=enze5088/Chatterbox&type=Date)](https://star-history.com/#enze5088/Chatterbox&Date)
