#模拟百度翻译
from urllib import request, parse
import json

baseurl = "https://fanyi.baidu.com/sug"

kw = input("请输入要翻译的词汇：")
data = {
    'kw': kw
}
data = parse.urlencode(data).encode("utf-8")

headers = {
    #使用post请求，至少包含content-length
    'Content-Length': len(data)
}

req = request.Request(url=baseurl, data=data, headers=headers)
rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8') #获取返回的json数据
dict_data = json.loads(json_data)    #将json数据loads为字典
count = 0
for item in dict_data['data']:
    print(item['k'], '----', item['v'])
    count = count+1
    if count == 4:
        break

