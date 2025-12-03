import threading

def say_hi(word):
    print('Hello %s!' % word)


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=say_hi,args=('loo',)) #创建工作线程
        t.start() #启动工资线程  target(*args)