import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'smartresult'
data['client'] = 'fanyideskweb'
data['salt'] = '15613879526883'
data['sign'] = '49b4448d210728122f0d5c039924bbdd'
data['ts'] = '1561387952688'
data['bv'] = 'f4d62a2579ebb44874d7ef93ba47e822'
data['ts'] = '1561387952688'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'


data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)  # 爬取url相应信息


# 网上爬取后的数据读取出来是json的形式：json把python认可的数据结构封装为字符串的形式
html = response.read().decode('utf-8')  # 解码为 utf-8


# print(html)
# 将json形式转换为认可的数据结构形式
target = json.loads(html)


# print(target)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
