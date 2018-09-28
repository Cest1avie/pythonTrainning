import requests
import re
from bs4 import BeautifulSoup

#设置请求头
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

#用列表生成器构造url列表
urls = ['https://www.pexels.com/?page={0}'.format(str(i)) for i in range(1,5)]
#用暂时存放图片资源的列表
photos = []

for url in urls:
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml') #将网页源代码解析为lxml
    images = soup.select('article.photo-item > a.js-photo-link > img') #用css选择器选择出图片的img标签
    for img in images:
        photo = img.get('src')  #将img标签的src属性值存入列表中
        photos.append(photo)

path = 'D:\python\\test\\'

for photoSrc in photos:
    data = requests.get(photoSrc, headers=headers)
    photoName = re.findall(r'/photos/(\d+)/pexels', photoSrc)
    print(photoName)
    if photoName:
        fp = open(path + photoName[0] +'.jpeg', 'wb')
        fp.write(data.content)
        fp.close()
