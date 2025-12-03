from urllib import request
html=  request.urlopen('http://www.baidu.com')
print(html.read(10))