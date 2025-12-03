import os
import time

print('starting')
ret_val=os.fork()

if ret_val:
    print('in parent')
    time.sleep(60)
    print('done')
else:
    print('in child')
    time.sleep(15)
    print('done')
