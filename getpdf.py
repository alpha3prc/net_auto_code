import urllib.request
html = urllib.request.urlopen('http://172.40.50.116/python.pdf')
fobj = open('/tmp/python.pdf', 'ab')
while True:
    data = html.read(4096)
    if not data:
        break
    fobj.write(data)
fobj.close()