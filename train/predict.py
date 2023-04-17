from tool.predicter import Predicter

messages = '[{"role": "user","content": "{}"},{"role": "assistant", "content":'
def main():
    model_path = './result/total/'
    chatbot = Predicter(model_path)
    messages_in = messages.format('你好')
    r = chatbot(text='m')
    print(r)


if __name__ == '__main__':
    main()