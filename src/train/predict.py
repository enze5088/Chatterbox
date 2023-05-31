import json

from tool.predicter import Predicter

messages = [{'role':'user','content': {}},{'role':'assistant','content':""}]
def main():
    model_path = './result/total/'
    chatbot = Predicter(model_path,device='cuda:0')
    messages[0]['content'] = '你好'
    messages_in = "<s>" + str(messages)

    messages_in = messages_in[:-3]
    r = chatbot(text=messages_in)
    # print(r[0])
    r = r[0].split('<\s>')
    # print(r)
    for item in r:
        try:
            item = eval(item)
            print(item)
        except:
            print(item)
    # r[0] = r[0].replace('<s>', '')
    # r_item = eval(r[0])
    # content = r_item[-1]['content']
    # print(content)



if __name__ == '__main__':
    main()