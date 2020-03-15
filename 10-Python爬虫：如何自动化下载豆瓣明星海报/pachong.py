from urllib.request import urlopen, Request
import requests
import json
import urllib

query = '葛优'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def download(src, id):
    """下载图片"""
    dir = './' + str(id) + '.jpg'
    save = False
    try:
        # 爬虫注意休息，当心反爬
        # 测试图片链接没有被网站设置反爬
        pic = requests.get(src, timeout=10)
        save = True
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
    if save:
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()


# 下载200张得了，别爬的太猛
for i in range(0, 200, 20):
    # 'https://www.douban.com/j/search_photo?q=%E8%91%9B%E4%BC%98&limit=20&start=0'
    # 对中文进行转码 urllib.parse.quote(query)
    url = 'https://www.douban.com/j/search_photo?q=' + urllib.parse.quote(query) + '&limit=20&start=' + str(i)
    # 上面的链接被网站设置反爬 requests.get(url) 已经无法使用
    html = Request(url, headers=headers)
    res = urlopen(html).read()
    response = json.loads(res)
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])
