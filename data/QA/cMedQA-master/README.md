# cMedQA v1.0
This is the dataset for Chinese community medical question answering. The dataset is in version 1.0 and is available for non-commercial research. We will update and expand the database from time to time. In order to protect the privacy, the data is anonymized and no personal information is included.

# Update

The newest version of cMedQA now comes to v2.0. You can [click here](https://github.com/zhangsheng93/cMedQA2)


# Overview

| DataSet | #Ques | #Ans | Ave. #words per Question |  Ave. #words per Answer| Ave. #characters per Question | Ave. #characters per Answer |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|Train|50,000|94,134|97|169|120|212|
|Dev|2,000|3,774|94|172|117|216|
|Test|2,000|3,835|96|168|119|211|
|Total|54,000|101,743|96|169|119|212|

* **questions.csv**  All Questions and their content.
* **answers.csv**  All Answers and their content.
* **train_candidates.txt** **dev_candidates.txt** **test_candidates.txt** The split of training set, development set and test set respectively.

# Paper
**Chinese Medical Question Answer Matching Using End-to-End Character-Level Multi-Scale CNNs** [link to the paper](http://www.mdpi.com/2076-3417/7/8/767)

Please cite our paper when you use the dataset.
```
@article{zhang2017chinese,
  title={Chinese Medical Question Answer Matching Using End-to-End Character-Level Multi-Scale CNNs},
  author={Zhang, Sheng and Zhang, Xin and Wang, Hui and Cheng, Jiajun and Li, Pei and Ding, Zhaoyun},
  journal={Applied Sciences},
  volume={7},
  number={8},
  pages={767},
  year={2017},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```
