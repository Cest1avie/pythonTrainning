from selenium import webdriver
browser = webdriver.Chrome()
j = browser.get('https://www.douban.com/')
browser.implicitly_wait(5)
browser.find_element_by_id('form_email').clear()
browser.find_element_by_id('form_email').send_keys('15926488894')
browser.find_element_by_id('form_password').clear()
browser.find_element_by_id('form_password').send_keys('hustfz23.')
browser.find_element_by_class_name('bn-submit').click()
print(browser.page_source)