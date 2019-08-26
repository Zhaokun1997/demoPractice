import urllib.request
import os


# import random


# 打开一个请求
def url_open(url):
    req = urllib.request.Request(url)
    # 修改 header 来模拟浏览器访问，便于隐藏（如果是利用python来访问，User-Agent则为python的版本号）
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    # # 加入代理（代理的作用是避免一个ip对网站特定的信息进行多次访问，便于隐藏）
    # proxies = ['36.7.69.56:8060', '101.231.104.82:80', '103.218.2.159:8080']
    # proxy = random.choice(proxies)
    # proxy_support = urllib.request.ProxyHandler({'http': proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()

    print(url)
    return html


# 获取图片对应的索引 num
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]


# 找到每一张图片的 src
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:  # 若可以找到 a
        b = html.find('.jpg', a, a + 255)  # 后半段标签的起始位置为 a 的起始地址，a+255测试限制是否超出整个页面范围
        if b != -1:  # 若可以找到 b
            img_addrs.append('http:' + html[a + 9:b + 4])
        else:  # 若找不到b
            b = a + 9
        a = html.find('img src=', b)
    for each in img_addrs:
        print(each)
    return img_addrs


# 保存图片到文件夹中
def save_imgs(img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]

        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


# 主方法
def download_mm(folder='OOXX', pages=5):
    os.mkdir(folder)  # 创建文件夹
    os.chdir(folder)  # 更改当前文件夹路径

    url = "http://jandan.net/ooxx/"  # 目标站点
    page_num = int(get_page(url))  # 获取页面图片的num

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'  # 获取对应页号图片网站页面的url
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)


if __name__ == '__main__':
    download_mm()
