import requests
import json

query = '葛优'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def download(src, id):
    """下载图片"""
    dir = './' + str(id) + '.jpg'
    save = False
    try:
        pic = requests.get(src, timeout=10)
        save = True
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
    if save:
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()


# 下载80张得了，别爬的太猛
for i in range(0, 80, 20):
    # 'https://www.douban.com/j/search_photo?q=%E8%91%9B%E4%BC%98&limit=20&start=0'
    # 对中文进行转码 urllib.parse.quote(query)
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url, headers=headers)
    res = html.text
    response = json.loads(res)
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])
