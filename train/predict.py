import json

from tool.predicter import Predicter

messages = [{'role':'user','content': {}},{'role':'assistant','content':""}]
def main():
    model_path = './result/checkpoints/'
    chatbot = Predicter(model_path,device='cpu')
    messages[0]['content'] = '你好'
    messages_in = "<s>" + str(messages)

    messages_in = messages_in[:-3]
    r = chatbot(text=messages_in)
    r = r[0].split('<\s>')[0].replace('<s>','')
    print(r)
    r_item = eval(r)
    content = r_item[-1]['content']
    print(content)



if __name__ == '__main__':
    main()