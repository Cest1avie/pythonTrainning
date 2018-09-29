import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient() #mongo server
songs = client.hello.songs #选择数据库 和 集合
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_info(url):
    #请求url
    html_data = requests.get(url, headers = headers)
    #解析为lxml
    soup = BeautifulSoup(html_data.text, 'lxml')
    #css选择器选择需要的标签
    ranks = soup.select('.pc_temp_num')
    times = soup.select('.pc_temp_time')
    titles = soup.select('.pc_temp_songlist > ul > li > a')
    for rank, title, song_time in zip(ranks, titles, times):
        data = {
            'rank':int(rank.get_text().strip()),
            'singer': title.get_text().split('-')[0].strip(),
            'song': title.get_text().split('-')[1].strip(),
            'time': song_time.get_text().strip()
        }
        #向mongodb的songs集合中插入数据
        songs.insert(data)
        print(data)


if __name__ == '__main__':
    for i in range(0,23):
        url = 'http://www.kugou.com/yy/rank/home/{0}-8888.html?from=rank'.format(i+1)
        get_info(url)
        time.sleep(2) #请求一次休息两秒 防止被禁止访问
