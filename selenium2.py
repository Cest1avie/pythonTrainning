from selenium import webdriver
#获取chrome浏览器操作对象
driver = webdriver.Chrome()
#打开网址---简书网的一篇文章
driver.get('https://www.jianshu.com/p/aa113d04b732')
driver.implicitly_wait(10)
# 获取作者的名字
author = driver.find_element_by_xpath('//span[@class="name"]/a').text
# 获取文章发布的时间
time = driver.find_element_by_xpath('//span[@class="publish-time"]').text
# 获取文章的字数
wordage = driver.find_element_by_xpath('//span[@class="wordage"]').text
# 获取文章的观看人数
views_count = driver.find_element_by_xpath('//span[@class="views-count"]').text
# 获取文章的评论数
comments_count = driver.find_element_by_xpath('//span[@class="comments-count"]').text
# 获取文章的喜欢人数
like = driver.find_element_by_xpath('//span[@class="likes-count"]').text
# 获取被那些专题收录 注意elements和element 坑啊
include_names = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
for i in include_names:
    print(i.text)
print(author,time,wordage,views_count,like)