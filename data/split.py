import csv
import json
import os
from random import shuffle, sample

from joblib import Parallel, delayed

model_path = '../train/model_file/bloomz-1b-zh/'
from tqdm import tqdm
from transformers import AutoTokenizer

MAX_LENGTH = 700
Batch_Len = int(MAX_LENGTH // 5)
random_seq = ['请继续', '继续讲', '往下说', '请继续讲', '请继续说']
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]


def single_job(name, output_dir):
    # train_writer = csv.writer(open(output_dir + 'train_datasets.csv', 'a'), delimiter='\t')
    # test_writer = csv.writer(open(output_dir + 'test_datasets.csv', 'a'), delimiter='\t')
    data = []
    too_long = 0
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    for line in tqdm(open(name)):
        line = json.loads(line)
        prompt = line['prompt']
        target = line['output']
        target = tokenizer.tokenize(target)
        source = line['source']

        inputs = [{"role": "user", "content": prompt}, {"role": "assistant", "content": line['output']}]

        if len(tokenizer.tokenize(prompt)) > MAX_LENGTH // 5:
            too_long += 1
            continue

        if len(target) > MAX_LENGTH * 10:
            too_long += 1
            continue

        inputs_seq = str(inputs)
        inputs_seq = "<s>" + inputs_seq + "<\s>"
        if len(tokenizer.tokenize(inputs_seq)) < MAX_LENGTH:
            line = [inputs_seq, source]
            data.append(line)
        else:
            target_list = [target[i:i + Batch_Len] for i in range(0, len(target), Batch_Len)]
            inputs_list = [{"role": "user", "content": prompt},
                           {"role": "assistant", "content": tokenizer.convert_tokens_to_string(target_list[0])}]
            # inputs_seq = json.dumps(inputs_list, ensure_ascii=False)
            inputs_seq = str(inputs_seq)
            inputs_seq = "<s>" + inputs_seq + "<\s>"
            line = [inputs_seq, source]
            data.append(line)
            for item in target_list[1:]:
                item = tokenizer.convert_tokens_to_string(item)
                inputs_item = [{"role": "user", "content": sample(random_seq, 1)[0]},
                               {"role": "assistant", "content": item}]
                inputs_list.extend(inputs_item)
                inputs = [inputs_list[0], inputs_list[-3], inputs_list[-2], inputs_list[-1]]
                inputs_seq = str(inputs)
                inputs_seq = "<s>" + inputs_seq + "<\s>"
                if len(tokenizer.tokenize(inputs_seq)) > MAX_LENGTH:
                    # print(inputs_seq)
                    too_long += 1
                line = [inputs_seq, source]
                data.append(line)
    return data, too_long


def main(in_dir='./collect_datasets/', output_dir='./datasets/'):
    file_names = os.listdir(in_dir)
    file_names = ['firefly.txt', 'Belle.txt', 'alpaca_gpt4_data_zh.txt']
    file_names = ['alpaca_gpt4_data_zh.txt']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    train_fin = open(output_dir + 'train_datasets.csv', 'w')
    test_fin = open(output_dir + 'test_datasets.csv', 'w')
    train_writer = csv.writer(train_fin, delimiter='\t')
    test_writer = csv.writer(test_fin, delimiter='\t')
    data = []
    title = ['inputs', 'source']

    train_writer.writerow(title)
    test_writer.writerow(title)
    job_nums = len(file_names) if len(file_names) < 10 else 10
    names = [in_dir + name for name in file_names]
    result = Parallel(n_jobs=job_nums) \
        (delayed(single_job)(split_block, output_dir) for split_block in tqdm(names))
    too_long = 0
    for item in result:
        data.extend(item[0])
        too_long += item[1]
    shuffle(data)
    print(len(data), too_long)
    split_num = int(len(data) * 0.005)
    train_data = data[:-split_num]
    test_data = data[-split_num:]
    train_writer.writerows(train_data)
    test_writer.writerows(test_data)


if __name__ == '__main__':
    main()
