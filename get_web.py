import os
import wget
import re
import urllib.error

def get_url(fname, patt, charset):
    "用于在指定的文件中取出所有的模式,返回一个列表"
    result = []
    # print('result:',result)
    cpatt = re.compile(patt)

    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result

if __name__ == "__main__":
    path = "/home/loo/net_auto/tmp/163"
    fname = "/home/loo/net_auto/tmp/163/163.html"
    url = "http://www.163.com"
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(fname):
        wget.download(url, fname)

    url_patt = "(http|https)://[\w./-]+\.(jpg|jpeg|png|gif)"
    img_list = get_url(fname, url_patt, 'utf-8')
    # print(img_list)
    for img_url in img_list:
        try:
            wget.download(img_url,path)
        except urllib.error.HTTPError as e:
            print('\n错误链接 %s', img_url)
        except Exception as e:
            print('下载错误')