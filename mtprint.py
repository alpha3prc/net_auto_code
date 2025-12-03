# 主线程生成工作线程
# 具体的任务由工作线程执行

import threading

def say_hi(tmp):
    print('hello %s' % tmp)

if __name__=='__main__':
    for i in range(3):
        t=threading.Thread(target=say_hi,args=('tedu',))
        t.start()