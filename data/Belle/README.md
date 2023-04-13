---
license: gpl-3.0
task_categories:
- text2text-generation
language:
- zh
size_categories:
- 100K<n<1M
---

## 内容
包含约100万条由[BELLE](https://github.com/LianjiaTech/BELLE)项目生成的中文指令数据。

## 样例
```
{
  "instruction": "给定一个文字输入，将其中的所有数字加1。\n“明天的会议在9点开始，记得准时到达。”\n",
  "input": "",
  "output": "“明天的会议在10点开始，记得准时到达。”"
}
```
### 字段：
```
instruction: 指令
input: 输入（本数据集均为空）
output: 输出
```

## 使用限制
仅允许将此数据集及使用此数据集生成的衍生物用于研究目的，不得用于商业，以及其他会对社会带来危害的用途。
本数据集不代表任何一方的立场、利益或想法，无关任何团体的任何类型的主张。因使用本数据集带来的任何损害、纠纷，本项目不承担任何责任。
