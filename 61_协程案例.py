# 案例
from gevent import monkey

monkey.patch_all()  # 此处的猴子补丁需要在导入requests包之前完成补丁操作
import requests
import gevent
import urllib.request


def download(url):
    # response = requests.get(url)
    response = urllib.request.urlopen(url)
    content = response.read()
    # content = response.text
    print('下载了{}的数据，长度：{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['http://www.163.com', 'http://www.qq.com', 'http://www.baidu.com']
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])

    gevent.joinall((g1, g2, g3))
