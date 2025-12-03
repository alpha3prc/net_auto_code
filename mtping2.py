import subprocess
import threading

class Ping:
    def __call__(self,host):
        result = subprocess.run(
            'ping -c2 %s > /dev/null 2>&1' % host, shell=True
        )
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips=['192.168.150.%s' % i for i in range(1, 255)]
    for ip in ips:
        t=threading.Thread(target=Ping(),args=(ip,))
        t.start()  #三个magic __init__,__str__,__call__
