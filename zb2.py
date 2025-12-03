import os
import time

print('starting')
ret_val=os.fork()
if ret_val:
    print('in parent')
    # result=os.waitpid(-1,0)
    result=os.waitpid(-1,1)     #不挂起父进程
    print(result)               #result 是元组:(子进程pid,0),(0,0)
    time.sleep(10)
    print('parent done')
else:
    print('in child')
    time.sleep(5)
    print('child done')