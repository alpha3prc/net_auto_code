import paramiko

def rcmd(host, user, passwd, port=22, cmds=None):
    # 创建ssh客户端实例，用于远程执行命令
    ssh = paramiko.SSHClient()
    # 自动接受服务器发来的密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(host, username=user, password=passwd, port=port)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmds)
    # 获取执行命令的输出和错误信息
    out = stdout.read()
    err = stderr.read()

    if out: # 如果输出非空
        print('[%s] OUT:\n%s' % (host, out.decode()))

    if err: # 如果错误非空
        print('[%s] ERROR:\n%s' % (host, err.decode()))

    # 关闭连接
    ssh.close()

if __name__ == '__main__':
    rcmd('127.0.0.1', 'root', 'redhat', cmds='id root; id zhangsan')
