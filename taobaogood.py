from selenium import webdriver
from lxml import etree
from pymongo import MongoClient
import time

# 获取mongodb的链接并建立goods集合
client = MongoClient()
goods = client.hello.goods

# selenium连接Firefox
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()

def get_info(url,page):
    # page仅仅用作判断，表示需要爬取指定页数的数据
    page = page + 1
    driver.get(url)
    driver.implicitly_wait(10)
    # 用etree解析网页源码
    selector = etree.HTML(driver.page_source)
    # infos为返回的对象列表
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        # info是一个额etree对象，可直接对该节点下的元素进行xpath检索
        good = info.xpath('div/div/div/a/img/@alt')[0] #/div/div/div/a/aimg/@alt
        price = int(info.xpath('div/div/div/strong/text()')[0]) #记得存入int型数据方便后来进行排序
        shop = info.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')[0] #css下标从1开始
        address = info.xpath('div[2]/div[3]/div[2]/text()')[0]
        dealNum = info.xpath('div[2]/div[1]/div[2]/text()')
        # 判断一下交易数量是否存在，有的商品还没有交易数量
        if dealNum:
            dealNum = int(dealNum[0].split('人')[0])
        else:
            dealNum = 0
        goodInfo = {
            'good': good,
            'price': price,
            'shop': shop,
            'address':address,
            'dealNum':dealNum
        }
        # 将数据插入mongodb
        goods.insert(goodInfo)
    if page <11:
        next_page(url,page)
    else:
        pass

def next_page(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(3)
    get_info(driver.current_url,page)


if __name__ == '__main__':
    url = 'https://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)  #设置响应等待时间
    # 找到搜索框并输入男士短袖，然后点击查询按钮
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')
    driver.find_element_by_class_name('btn-search').click()
    get_info(driver.current_url,1)