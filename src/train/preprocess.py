import csv
import time

import transformers
from datasets import load_dataset
from joblib import Parallel, delayed
from tqdm import tqdm
from transformers import AutoTokenizer
from transformers.testing_utils import CaptureLogger
from itertools import chain
import sys

csv.field_size_limit(sys.maxsize // 10)
#数据基础处理目录
base_dir = './data/'
# 设置为自己的模型路径
model_path = "./model_files/LLaMA-zh-base"
# 设置为自己的文本长度
block_size = 512
job_nums = 300
GroupFlag = True
print('Group Data:{};job num:{}'.format(GroupFlag, job_nums))


def Process_Lines(lines, out_path, proc_num):
    TokensNum = 0
    tok = AutoTokenizer.from_pretrained(model_path)
    writer = csv.writer(open(out_path, 'a'))
    for text_id in tqdm(range(0, len(lines)), disable=proc_num, desc='process'):
        EncodeText = tok.encode_plus(lines[text_id])['input_ids']
        if len(EncodeText) > 1:
            EncodeText = [1] + EncodeText + [2]
        EncodeTexts = [EncodeText[i: i + block_size] for i in range(0, len(EncodeText), block_size)]
        for item in EncodeTexts:
            if len(item) >= 1:
                writer.writerow([item])
                TokensNum += len(item)
    return TokensNum


def Group_Process_Lines(lines, out_path, proc_num):
    MinOutNum = 2
    TokensNum = 0
    tok = AutoTokenizer.from_pretrained(model_path)
    writer = csv.writer(open(out_path, 'a'))
    Group = []
    for text_id in tqdm(range(0, len(lines)), disable=proc_num, desc='process'):
        EncodeText = tok.encode_plus(lines[text_id])['input_ids']
        if len(EncodeText) > 1:
            EncodeText = [1] + EncodeText + [2]
            Group.extend(EncodeText)

        if len(Group) > block_size * 20:
            EncodeTexts = [Group[i: i + block_size] for i in range(0, len(Group), block_size)]
            for item in EncodeTexts:
                if len(item) >= MinOutNum:
                    writer.writerow([item])
                    TokensNum += len(item)
            Group = []

    if len(Group) > 0:
        EncodeTexts = [Group[i: i + block_size] for i in range(0, len(Group), block_size)]
        for item in EncodeTexts:
            if len(item) >= MinOutNum:
                writer.writerow([item])
                TokensNum += len(item)

    return TokensNum


def palled_job_each(total_list, job_nums, out_path):
    """
    :param total_list: A list of paths to all images that need to be processed
    :param job_nums: Number of threads enabled
    :param out_path: output path
    :return: None
    """
    bs = len(total_list) // job_nums
    Process_Func = Group_Process_Lines if GroupFlag else Process_Lines
    total_block = [total_list[i:i + bs] for i in range(0, len(total_list), bs)]
    result = Parallel(n_jobs=job_nums) \
        (delayed(Process_Func)(total_block[i], out_path, len(total_block) - i - 1) for i in range(len(total_block)))
    return sum(result)


def Process_File(in_file, out_file):
    reader = csv.reader(open(in_file), delimiter='\t')
    title = reader.__next__()
    writer = csv.writer(open(out_file, 'w'), delimiter='\t')
    writer.writerow(['text'])
    del writer
    data = []
    TotalTokens = 0
    theld = 30000000
    for line in tqdm(reader, desc='reading'):
        data.append(line[0])
        if len(data) >= theld:
            r = palled_job_each(data, job_nums=job_nums, out_path=out_file)
            TotalTokens += r
            data = []

    if len(data) >= 0:
        r = palled_job_each(data, job_nums=job_nums if len(data) > job_nums else len(data), out_path=out_file)
        TotalTokens += r
        data = []

    print('Total Tokens Number:', TotalTokens)


if __name__ == '__main__':
    print('PreProcess Data')

    begin = time.time()
    train_file = base_dir + "total.csv"
    validation_file = base_dir + "test.csv"
    out_file = base_dir + '/output/train.csv'
    Process_File(train_file, out_file=out_file)
    out_file = base_dir + '/output/test.csv'
    Process_File(validation_file, out_file)
    end = time.time()
    print(end - begin)
