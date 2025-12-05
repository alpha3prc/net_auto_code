import os
import re
import urllib.request # 1. 引入 request 模块
import urllib.error

def get_url(fname, patt, charset):
    "用于在指定的文件中取出所有的模式,返回一个列表"
    result = []
    cpatt = re.compile(patt)
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result

# 2. 封装一个简单的下载函数，替代 wget
def download(url, save_path, headers=None):
    if headers is None:
        headers = {}
    # 核心：通过 urllib.request.Request 传参携带 headers
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as web, open(save_path, 'wb') as outfile:
        outfile.write(web.read())

if __name__ == "__main__":
    path = "/home/loo/net_auto/tmp/163"
    fname = "/home/loo/net_auto/tmp/163/163.html"
    url = "http://www.163.com"
    
    # 3. 定义 headers 字典
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(fname):
        # 调用自定义下载函数，传入 headers
        download(url, fname, headers)

    url_patt = "(http|https)://[\w./-]+\.(jpg|jpeg|png|gif)"
    img_list = get_url(fname, url_patt, 'utf-8')

    for img_url in img_list:
        # 拼接文件名
        img_name = os.path.join(path, os.path.basename(img_url))
        try:
            # 调用自定义下载函数，传入 headers
            download(img_url, img_name, headers)
        except urllib.error.HTTPError as e:
            print('\n错误链接 %s' % img_url)
        except Exception as e:
            print('下载错误', e)
