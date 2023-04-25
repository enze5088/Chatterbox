import csv
import json
import os
import random
import sys

from tqdm import tqdm

csv.field_size_limit(sys.maxsize // 1000)


def webtext2019zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'),delimiter='\t')
    base_dir = "./QA/web_text_zh/"
    name_list = os.listdir(base_dir)
    for name in name_list:
        dir_in = base_dir + name
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
            line = [prompt + ans, datasets_name]
            writer.writerow(line)


def rmrb():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'),delimiter='\t')
    base_dir = "./pretrain_datasets/rmrb/"
    name_list = os.listdir(base_dir)
    for name in name_list:
        dir_in = base_dir + name
        reader = csv.reader(open(dir_in),delimiter='\t')
        title = reader.__next__()
        for line in tqdm(reader):
            content = line[1]
            if len(content.replace(' ','')) < 5:
                continue
            line = [content , datasets_name]
            writer.writerow(line)

def wiki_zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'), delimiter='\t')
    base_dir = "./QA/{}/".format(datasets_name)
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
                content = "\\n ".join(contents[:])
                # ans = content
                line = [content, datasets_name]
                writer.writerow(line)

def clean(text):
    text = text.replace('// // // //','')
    text = text.replace('(本文内容来源于网络 版权归原作者所有)','')
    return text

def new2016zh():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'), delimiter='\t')
    base_dir = './pretrain_datasets/new2016zh/'
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = root + '/' + file
            for line in open(file_path):
                line = json.loads(line)
                content = line['content']
                content = clean(content)
                line = [content, datasets_name]

                writer.writerow(line)


def csl():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'), delimiter='\t')
    base_dir = './pretrain_datasets/csl/'
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = root + '/' + file
            for line in tqdm(csv.reader(open(file_path), delimiter='\t')):
                content = line[1]
                line = [content, datasets_name]
                writer.writerow(line)


def cat_sina_news():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'), delimiter='\t')
    base_dir = './pretrain_datasets/csl/'
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = root + '/' + file
            for line in tqdm(csv.reader(open(file_path), delimiter='\t')):
                content = line[1]
                line = [content, datasets_name]
                writer.writerow(line)


def cat_pretrain_data():
    in_dir = './pretrain_datasets/output/'
    out_dir = './pretrain_datasets/datasets/'
    names = os.listdir(in_dir)
    title = ['text', 'source']
    train_writer = csv.writer(open(out_dir + 'train.csv', 'w'), delimiter='\t')
    test_writer = csv.writer(open(out_dir + 'test.csv', 'w'), delimiter='\t')
    train_writer.writerow(title)
    test_writer.writerow(title)
    names.sort()
    for name in tqdm(names):
        print(name)
        name = in_dir + name
        reader = csv.reader((line.replace('\0', '') for line in open(name, errors='ignore')), delimiter='\t')
        for line in tqdm(reader):
            line[0] = line[0].relace('\t',' ')
            p = random.random()
            if len(line[0].replace(' ', '')) < 5:
                continue
            if p < 0.001:
                test_writer.writerow(line)
            else:
                train_writer.writerow(line)


def Belle():
    datasets_name = sys._getframe().f_code.co_name
    writer = csv.writer(open('./pretrain_datasets/output/{}.txt'.format(datasets_name), 'w'), delimiter='\t')
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
            content = prompt + ans
            content = content.replace('\n',' \\n ')
            # item = {"prompt": prompt, "output": ans, "source": datasets_name}
            # item = json.dumps(item, ensure_ascii=False)
            line = [content, datasets_name]
            writer.writerow(line)
    print('max_len:', max_len)
    print(max_ans)


if __name__ == '__main__':
    # webtext2019zh()
    # wiki_zh()
    # new2016zh()
    # csl()
    # Belle()
    # webtext2019zh()
    # rmrb()
    cat_pretrain_data()
