import re
import time
from multiprocessing import Pool
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

def re_scraper(url):
    res = requests.get(url,headers = headers)
    names = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote">.*?<i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i>',res.text,re.S)
    for name,content,laugh,comment in zip(names,contents,laughs,comments):
        info = {
            'name':name,
            'content':content,
            'laugh':laugh,
             'comment':comment
        }


if __name__ == '__main__':
    urls = ["https://www.qiushibaike.com/8hr/page/{0}/".format(str(i)) for i in range(1,35)] #列表生成器
    start1 = time.time()
    for url in urls:
        re_scraper(url)
    end1 = time.time()
    print('串行性爬虫耗时：',end1-start1)

    start2 = time.time()
    pool = Pool(processes=2) #构建两个进程
    pool.map(re_scraper, urls)
    end2 = time.time()
    print('2进程爬虫耗时：', end2 - start2)

    start3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper, urls)
    end3 = time.time()
    print('4进程爬虫耗时：', end3 - start3)
