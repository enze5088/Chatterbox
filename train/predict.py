import json

from tool.predicter import Predicter

messages = [{'role':'user','content': {}},{'role':'assistant','content':""}]
def main():
    model_path = './result/checkpoints/'
    chatbot = Predicter(model_path)
    messages[0]['content'] = '你好'

    messages_in = "<s>" + str(messages)
    print(messages_in)
    messages_in = messages_in[:-3]
    print(messages_in)
    r = chatbot(text=messages_in)
    print(r[0])
    r = r[0].split('<\s>')[0].replace('<s>','')

    print(r)
    messages_in = messages_in.replace('<s>','').replace(' ','')
    r = r.replace(messages_in,'').replace("'}}]",'').replace("')}]",'')
    print(r)


if __name__ == '__main__':
    main()