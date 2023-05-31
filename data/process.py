import csv
import json
import os
import random
import sys
from random import sample

from tqdm import tqdm

csv.field_size_limit(sys.maxsize // 10)


def cMedQA1():
    train_data = csv.reader(open("./QA/cMedQA-master/train_candidates.txt"))
    test_data = csv.reader(open("./QA/cMedQA-master/test_candidates.txt"))
    questions_data = csv.reader(open("./QA/cMedQA-master/questions.csv"))
    answers_data = csv.reader(open("./QA/cMedQA-master/answers.csv"))

    questions = dict()
    questions_data.__next__()
    for line in questions_data:
        que_id = line[0]
        content = line[1]
        big_cate = line[2]
        small_cate = line[3]
        questions[que_id] = [content, big_cate, small_cate]
    answers = dict()
    answers_data.__next__()
    for line in answers_data:
        ans_id = line[0]
        que_id = line[1]
        content = line[2]
        answers[ans_id] = content

    writer = open('./collect_datasets/cMedQA.txt', 'w')
    used_set = set()
    title = train_data.__next__()
    for line in train_data:
        que_id = line[0]
        ans_id = line[1]
        used_id = "que:{},ans_id{}".format(que_id, ans_id)

        if used_id in used_set:
            continue
        else:
            used_set.add(used_id)
        # print(que_id, ans_id)
        que = questions[que_id][0]
        ans = answers[ans_id].replace("欢迎您下次再咨询", "")
        item = {"prompt": que, "output": ans, "source": "cMedQA-1"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')

    title = test_data.__next__()

    for line in test_data:
        # print(line)
        que_id = line[0]
        ans_id = line[1]
        label = line[-1]
        if label == '0':
            continue
        used_id = "que:{},ans_id{}".format(que_id, ans_id)

        if used_id in used_set:
            continue
        else:
            used_set.add(used_id)

        que = questions[que_id][0]
        ans = answers[ans_id].replace("欢迎您下次再咨询", "")

        item = {"prompt": que, "output": ans, "source": "cMedQA-1"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')


def cMedQA2():
    train_data = csv.reader(open("./QA/cMedQA2-master/train_candidates.txt"))
    test_data = csv.reader(open("./QA/cMedQA2-master/test_candidates.txt"))
    questions_data = csv.reader(open("./QA/cMedQA2-master/question.csv"))
    answers_data = csv.reader(open("./QA/cMedQA2-master/answer.csv"))

    questions = dict()
    questions_data.__next__()

    for line in questions_data:
        # print(line)
        que_id = line[0]
        content = line[1]
        # big_cate = line[2]
        # small_cate = line[3]
        questions[que_id] = [content]
    answers = dict()
    answers_data.__next__()
    for line in answers_data:
        ans_id = line[0]
        que_id = line[1]
        content = line[2]
        answers[ans_id] = content

    writer = open('./collect_datasets/cMedQA2.txt', 'w')
    used_set = set()
    title = train_data.__next__()
    for line in train_data:
        que_id = line[0]
        ans_id = line[1]
        used_id = "que:{},ans_id{}".format(que_id, ans_id)
        if used_id in used_set:
            continue
        else:
            used_set.add(used_id)
        # print(que_id, ans_id)
        que = questions[que_id][0]
        ans = answers[ans_id].replace("欢迎您下次再咨询", "")
        item = {"prompt": que, "output": ans, "source": "cMedQA-2"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')

    title = test_data.__next__()

    for line in test_data:
        # print(line)
        que_id = line[0]
        ans_id = line[1]
        label = line[-1]
        if label == '0':
            continue
        used_id = "que:{},ans_id{}".format(que_id, ans_id)

        if used_id in used_set:
            continue
        else:
            used_set.add(used_id)

        que = questions[que_id][0]
        ans = answers[ans_id].replace("欢迎您下次再咨询", "")

        item = {"prompt": que, "output": ans, "source": "cMedQA-2"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')


def webMedQA():
    writer = open('./collect_datasets/webMedQA.txt', 'w')
    train_in = csv.reader(open("./QA/webMedQA-master/medQA.train.txt"), delimiter='\t')
    count = 0
    count2 = 0
    for line in tqdm(train_in):
        # print(line)
        label = line[1]
        question = line[3]
        ans = line[4]
        if int(label) == 1:
            item = {"prompt": question, "output": ans, "source": "webMedQA"}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
            count += 1
        elif int(label) == 0:
            count2 += 1
    print(count, count2)

    test_in = csv.reader(open("./QA/webMedQA-master/medQA.test.txt"), delimiter='\t')
    for line in tqdm(test_in):

        label = line[1]
        question = line[3]
        ans = line[4]
        if label == '1':
            item = {"prompt": question, "output": ans, "source": "webMedQA"}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')

    valid_in = csv.reader(open("./QA/webMedQA-master/medQA.valid.txt"), delimiter='\t')
    for line in tqdm(valid_in):
        label = line[1]
        question = line[3]
        ans = line[4]
        if label == '1':
            item = {"prompt": question, "output": ans, "source": "webMedQA"}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')


def baike_qa2019():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    train_in = open("./QA/baike_qa2019/baike_qa_train.json")
    for line in train_in:
        # print(line)
        line = json.loads(line)
        que = line['title']
        desc = line['desc']
        if str(desc).startswith(que.strip()):
            prompt = desc
        else:
            prompt = que + '' + desc
        ans = line['answer']
        # prompt = prompt.relace('\\r\\r','')
        # ans = ans.relace('\\r\\r','')
        item = {"prompt": prompt, "output": ans, "source": "baike_qa2019"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')

    valid_in = open("./QA/baike_qa2019/baike_qa_valid.json")
    for line in valid_in:
        line = json.loads(line)
        que = line['title']
        desc = line['desc']
        if str(desc).startswith(que.strip()):
            prompt = desc
        else:
            prompt = que + '' + desc
        ans = line['answer']
        # prompt = prompt.relace('\\r\\r','')
        # ans = ans.relace('\\r\\r','')
        item = {"prompt": prompt, "output": ans, "source": "baike_qa2019"}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')

    writer.close()


def MSRA_NER():
    datasets_name = sys._getframe().f_code.co_name
    NER_MAP = {
        'LOC': '地理类实体',
        'ORG': '组织类实体',
        'PER': '人物类实体',
    }

    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    in_list = ['train', 'test', 'val']
    base_dir = './NER/NER_MSRA/'
    ques_prompt_base = ["下面句话中包括了地理，组织，人物三类实体，请帮我对下面这句话做一下实体识别。",
                        "地理，组织，人物三类实体,实体识别一下这句话:", "实体识别一下下面这句话。",
                        "帮我标记一下下面这句话的实体：", "帮我解析一下这句话中的实体：", "这句话有那些实体？"
                        ]
    ans_prompt_base = ["上面这句话包括了以下几个实体: ", "实体有: ", "有以下几个实体: ", "", "这句话中的实体有 \\n\\n :"]
    for inp in in_list:
        input_dir = base_dir + inp + '/'
        sentences = open(input_dir + 'sentences.txt')
        tags = open(input_dir + 'tags.txt')
        for sentence, tag in zip(sentences, tags):
            ner_set = set()
            sentence = sentence.strip().split()
            tag = tag.strip().split()
            # print(sentence)
            begin = -1
            end = -1
            for s_id in range(len(sentence)):
                if not tag[s_id] == 'O':
                    if 'B' in tag[s_id]:
                        begin = s_id

                    if 'I' in tag[s_id]:
                        if s_id + 1 <= len(sentence):
                            if tag[s_id + 1] == 'O':
                                item = ''.join(sentence[begin:s_id + 1])
                                # print(item)
                                ner_type = NER_MAP[tag[begin].split('-')[-1]]
                                ner_set.add((item, ner_type))
                                begin = -1
                        else:
                            item = ''.join(sentence[begin:s_id + 1])
                            ner_type = NER_MAP[tag[begin].split('-')[-1]]
                            ner_set.add((item, ner_type))
                            begin = -1
            prompt = sample(ques_prompt_base, 1)[0] + "".join(sentence)
            if len(ner_set) > 0:
                ans = sample(ans_prompt_base, 1)[0]
                ans_base = ""
                if random.random() < 0.5:
                    for item in ner_set:
                        ans_base += "\\n " + "{} / {}。".format(item[0], item[1])
                else:
                    count = 0
                    for item in ner_set:
                        ans_base += "\\n " + str(count) + '.' + " {} / {}。".format(item[0], item[1])
                        count += 1
                ans = ans + ans_base
            else:
                ans = sample(['这句话中不包含实体', '这句话中不含有实体', '未发现实体'], 1)[0]

            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')

    writer.close()


def RMRB_NER():
    datasets_name = sys._getframe().f_code.co_name
    NER_MAP = {
        'PER': '人物类实体',
    }

    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    in_list = ['data_train.txt', 'data_test.txt', 'data_dev.txt']
    base_dir = './NER/RMRB_NER/'
    ques_prompt_base = ["请帮我对下面这句话做一下人物的实体识别。",
                        "实体识别一下这句话里的人:", "识别一下下面这句话都有哪些人物。",
                        "帮我标记一下下面这句话的人物实体：", "帮我解析一下这句话中的人物：", "这句话有那些人物实体？"
                        ]
    ans_prompt_base = ["上面这句话包括了以下几个人物类实体: ", "人物有: ", "有以下几个人物: ", "", "这句话中的人物类实体有 \\n\\n :"]
    for inp in in_list:
        input_dir = base_dir + inp
        sentences = []
        tags = []
        s_list = []
        t_list = []
        for line in csv.reader(open(input_dir), delimiter=' '):

            if len(line) == 0:
                sentences.append(s_list)
                tags.append(t_list)
                s_list = []
                t_list = []
            else:
                s_list.append(line[0])
                t_list.append(line[1])

        for sentence, tag in zip(sentences, tags):
            ner_set = set()
            if not len(sentence) == len(tag):
                print(sentence)
                print(tag)
                exit()
            # sentence = sentence.strip().split()
            # tag = tag.strip().split()
            # print(sentence)
            begin = -1
            end = -1
            for s_id in range(len(sentence)):
                if not tag[s_id] == 'O':
                    if 'B' in tag[s_id]:
                        begin = s_id

                    if 'I' in tag[s_id]:
                        if s_id + 1 < len(tag):
                            if tag[s_id + 1] == 'O':
                                item = ''.join(sentence[begin:s_id + 1])
                                # print(item)
                                ner_type = NER_MAP[tag[begin].split('-')[-1]]
                                ner_set.add((item, ner_type))
                                begin = -1
                        else:
                            item = ''.join(sentence[begin:s_id + 1])
                            ner_type = NER_MAP[tag[begin].split('-')[-1]]
                            ner_set.add((item, ner_type))
                            begin = -1
            prompt = sample(ques_prompt_base, 1)[0] + "".join(sentence)
            if len(ner_set) > 0:
                ans = sample(ans_prompt_base, 1)[0]
                ans_base = ""
                if random.random() < 0.5:
                    for item in ner_set:
                        ans_base += "\\n " + "{} / {}。".format(item[0], item[1])
                else:
                    count = 0
                    for item in ner_set:
                        ans_base += "\\n " + str(count) + '.' + " {} 。".format(item[0])
                        count += 1
                ans = ans + ans_base
            else:
                ans = sample(['这句话中不包含实体', '这句话中不含有实体', '未发现实体'], 1)[0]

            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')

    writer.close()


def cluener_public_NER():
    datasets_name = sys._getframe().f_code.co_name
    NER_MAP = {
        'address': '地址',
        'book': '书名',
        'company': '公司',
        'game': '游戏',
        'government': '政府',
        'movie': '电影',
        "name": "姓名",
        "organization": "组织机构",
        "position": "职位",
        "scene": "景点",
    }

    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    in_list = ['train.json', 'test.json', 'dev.json']
    base_dir = './NER/cluener_public/'
    ques_prompt_base = ["请帮我对下面这句话做一下实体识别。",
                        "实体识别一下这句话:", "实体识别一下下面这句话。",
                        "帮我标记一下下面这句话的实体：", "帮我解析一下这句话中的实体：", "这句话有那些实体？"
                        ]
    ans_prompt_base = ["上面这句话包括了以下几个实体: ", "实体有: ", "有以下几个实体: ", "", "这句话中的实体有 \\n\\n :"]
    for inp in in_list:
        input_dir = base_dir + inp
        for line in open(input_dir):
            line = json.loads(line)
            sentence = line['text']
            label = line.get('label', {})

            ner_set = set()
            # print(line)

            prompt = sample(ques_prompt_base, 1)[0] + "".join(sentence)
            for k, v in label.items():
                v_list = list(v.keys())
                for label_name in v_list:
                    ner_set.add((label_name, NER_MAP[k]))
            # print(ner_set)

            if len(ner_set) > 0:
                ans = sample(ans_prompt_base, 1)[0]
                ans_base = ""
                if random.random() < 0.5:
                    for item in ner_set:
                        ans_base += "\\n " + "{} / {}。".format(item[0], item[1])
                else:
                    count = 0
                    for item in ner_set:
                        ans_base += "\\n " + str(count) + '.' + " {} / {}。".format(item[0], item[1])
                        count += 1
                ans = ans + ans_base
            else:
                ans = sample(['这句话中不包含实体', '这句话中不含有实体', '未发现实体'], 1)[0]

            item = {"prompt": prompt, "output": ans, "source": datasets_name}

            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')

    writer.close()


def clean(text):
    text = text.relace('\\r\\r', ' ')
    text = text.relace('\\r', ' ')
    return text


def webtext2019zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./QA/web_text_zh/"
    name_list = os.listdir(base_dir)
    for name in name_list:
        dir_in = base_dir + name
        # print(dir_in)
        for line in tqdm(open(dir_in)):
            line = json.loads(line)
            title = line['title']
            desc = line['desc']
            if not desc == '':
                prompt = title + ' \\n ' + desc
            else:
                prompt = title
            ans = line['content']
            star = int(line['star'])
            if star < 5:
                continue
            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')


def bq_corpus():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./STS/{}/".format(datasets_name)
    file_list = os.listdir(base_dir)
    # print(file_list)
    qus_base = ["请问以下两句话是否相关？{} \\t {}",
                "这两句话含义一样么？{} \\n {}",
                "这两句话是否相关？{}  {}",
                "{} \\t  {}这句话含义是否和另一句一样？"]
    ans_true = ["这两句的表达含义一样", "这两句的表达含义基本一致", "这两句的表达含义一致"]
    ans_false = ["这两句话表达不一致的含义", '这两句话表达含义并不一样', "这两句话的含义不一致"]
    count = 0
    for file_name in file_list:
        file_in = base_dir + file_name
        for line in open(file_in):
            line = line.strip('\n').split('\t')
            if not len(line) == 3:
                # print(line)
                count += 1
                continue
            prompt = sample(qus_base, 1)[0].format(line[0], line[1])
            if int(line[2]):
                ans = sample(ans_true, 1)[0]
            else:
                ans = sample(ans_false, 1)[0]
            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
            # exit()
    writer.close()
    print(count)


def paws_x_zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./STS/{}/".format(datasets_name)
    file_list = os.listdir(base_dir)
    # print(file_list)
    qus_base = ["请问以下两句话是否相关？{} \\t {}",
                "这两句话含义一样么？{} \\n {}",
                "这两句话是否相关？{}  {}",
                "{} \\t  {}这句话含义是否和另一句一样？"]
    ans_true = ["这两句的表达含义一样", "这两句的表达含义基本一致", "这两句的表达含义一致"]
    ans_false = ["这两句话表达不一致的含义", '这两句话表达含义并不一样', "这两句话的含义不一致"]
    count = 0
    for file_name in file_list:
        file_in = base_dir + file_name
        for line in open(file_in):
            line = line.strip('\n').split('\t')
            if not len(line) == 3:
                # print(line)
                count += 1
                continue
            prompt = sample(qus_base, 1)[0].format(line[0], line[1])
            if int(line[2]):
                ans = sample(ans_true, 1)[0]
            else:
                ans = sample(ans_false, 1)[0]
            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
            # exit()
    writer.close()
    print(count)


def lcqmc():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./STS/{}/".format(datasets_name)
    file_list = os.listdir(base_dir)
    # print(file_list)
    qus_base = ["请问以下两句话是否相关？{} \\t {}",
                "这两句话含义一样么？{} \\n {}",
                "这两句话是否相关？{}  {}",
                "{} \\t  {}这句话含义是否和另一句一样？"]
    ans_true = ["这两句的表达含义一样", "这两句的表达含义基本一致", "这两句的表达含义一致"]
    ans_false = ["这两句话表达不一致的含义", '这两句话表达含义并不一样', "这两句话的含义不一致"]
    count = 0
    for file_name in file_list:
        file_in = base_dir + file_name
        for line in open(file_in):
            line = line.strip('\n').split('\t')
            if not len(line) == 3:
                # print(line)
                count += 1
                continue
            prompt = sample(qus_base, 1)[0].format(line[0], line[1])
            if int(line[2]):
                ans = sample(ans_true, 1)[0]
            else:
                ans = sample(ans_false, 1)[0]
            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
            # exit()
    writer.close()
    print(count)


def wiki_zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./QA/{}/".format(datasets_name)
    qus_base = ["{}是什么？", "{}是什么意思？", "{}是啥？", "请解释一下{}的含义？", "你知道{}是什么意思吗？", "{}表示了什么？",
                "什么是{}？", "你知道什么叫{}吗？", "你知道什么是{}吗？", "{}是什么意思？", ""]

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = root + '/' + file
            for line in open(file_path):
                line = json.loads(line)
                # print(line)

                title = line['title']

                content = line['text']
                content = content.replace("（）", '')
                contents = content.split('\n')
                contents = [seq for seq in contents if not seq == '']

                if len(contents) > 1 and contents[0] in contents[1]:
                    contents = contents[1:]
                content = "\\n ".join(contents[:40])
                prompt = sample(qus_base, 1)[0].format(title)
                ans = content
                item = {"prompt": prompt, "output": ans, "source": datasets_name}
                item = json.dumps(item, ensure_ascii=False)
                writer.write(item + '\n')


def alpaca_gpt4_data_zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./{}/{}.json".format(datasets_name, datasets_name)
    fin = open(base_dir)
    data = fin.readlines()
    data = ' '.join([line.replace('\n', '') for line in data])
    data = json.loads(data)
    max_len = 0
    max_ans = ''
    for line in data:

        prompt = line['instruction'] + line['input']
        ans = line['output']
        if len(ans) > max_len:
            max_len = len(ans)
            max_ans = ans

        item = {"prompt": prompt, "output": ans, "source": datasets_name}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')
    print('max_len:', max_len)
    print(max_ans)


def Belle():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    names = os.listdir("./{}/".format(datasets_name))
    for name in names:
        print(name)
        if 'README.md' == name:
            continue
        base_dir = "./{}/{}".format(datasets_name, name)
        fin = open(base_dir)
        max_len = 0
        max_ans = ''
        for line in tqdm(fin):
            line = json.loads(line)
            prompt = line['instruction'] + line['input']
            ans = line['output']
            if len(ans) > max_len:
                max_len = len(ans)
                max_ans = ans
            item = {"prompt": prompt, "output": ans, "source": datasets_name}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
    print('max_len:', max_len)
    print(max_ans)


# 1.1M
def firefly():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./{}/firefly-train-1.1M.jsonl".format(datasets_name)
    fin = open(base_dir)
    max_len = 0
    max_ans = ''
    for line in tqdm(fin):

        line = json.loads(line)
        # print(line)
        prompt = line['input']
        ans = line['target']
        if ans == 'nan':
            continue
        if len(str(ans)) > max_len:
            max_len = len(ans)
            max_ans = ans
        item = {"prompt": prompt, "output": ans, "source": datasets_name + ':' + line['kind']}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')
    print('max_len:', max_len)
    print(max_ans)

# 1.1M
def dolloy():
    datasets_name = sys._getframe().f_code.co_name
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir = "./{}/databricks-dolly-15k.jsonl".format(datasets_name)
    fin = open(base_dir)
    max_len = 0
    max_ans = ''
    for line in tqdm(fin):
        line = json.loads(line)
        prompt = line["instruction"]
        ans = line["context"] + ' ' + line["response"]
        # ans = ans.replace('\n','\\n')
        if ans == 'nan':
            continue
        if len(str(ans)) > max_len:
            max_len = len(ans)
            max_ans = ans
        item = {"prompt": prompt, "output": ans, "source": datasets_name + ':' + line["category"]}
        item = json.dumps(item, ensure_ascii=False)
        writer.write(item + '\n')
    print('max_len:', max_len)
    print(max_ans)

def moss():
    max_len = 0
    max_ans = ''
    datasets_name = sys._getframe().f_code.co_name
    datasets_dir = "./{}/".format(datasets_name)
    writer = open('./collect_datasets/{}.txt'.format(datasets_name), 'w')
    base_dir_list = os.listdir(datasets_dir)
    for base_dir in base_dir_list:
        base_dir = datasets_dir + base_dir
        print(base_dir)
        fin = open(base_dir)
        for lines in tqdm(fin):
            lines = json.loads(lines)
            print(type(lines))
            print(len(lines))
            exit()
            prompt = line["instruction"]
            ans = line["context"] + ' ' + line["response"]
            # ans = ans.replace('\n','\\n')
            if ans == 'nan':
                continue
            if len(str(ans)) > max_len:
                max_len = len(ans)
                max_ans = ans
            item = {"prompt": prompt, "output": ans, "source": datasets_name + ':' + line["category"]}
            item = json.dumps(item, ensure_ascii=False)
            writer.write(item + '\n')
    print('max_len:', max_len)
    print(max_ans)

if __name__ == '__main__':
    # cMedQA1()
    # cMedQA2()
    # webMedQA()
    # baike_qa2019()  #
    # webtext2019zh()
    # MSRA_NER()
    # RMRB_NER()
    # cluener_public_NER()
    # bq_corpus()
    # lcqmc()
    # paws_x_zh()
    # wiki_zh()
    # alpaca_gpt4_data_zh()
    # Belle()
    # firefly()
    # dolloy()
    # moss()
    print('process over')
