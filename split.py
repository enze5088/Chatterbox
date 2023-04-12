import csv
import json
import os
from random import shuffle

from tqdm import tqdm


def main(in_dir='./data/collect_datasets/',output_dir='./data/datasets/'):
    file_names = os.listdir(in_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    train_writer = csv.writer(open(output_dir+'train_datasets.csv','w'),delimiter='\t')
    test_writer = csv.writer(open(output_dir+'test_datasets.csv','w'),delimiter='\t')
    data = []
    title = ['inputs', 'target', 'source']
    train_writer.writerow(title)
    test_writer.writerow(title)
    for name in tqdm(file_names):
        print(name)
        name = in_dir + name
        for line in open(name):
            line = json.loads(line)
            # print(line)
            inputs = line['prompt']
            target = line['output']
            source = line['source']
            # print(line)
            line = [inputs,target,source]
            data.append(line)
    shuffle(data)
    split_num = int(len(data)*0.005)
    train_data = data[:-split_num]
    test_data = data[-split_num:]
    train_writer.writerows(train_data)
    test_writer.writerows(test_data)

if __name__ == '__main__':
    main()