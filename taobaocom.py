from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#用selenium模拟使用浏览器
driver = webdriver.Firefox()
driver.maximize_window()

if __name__ == '__main__':
    url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d92ERhVI&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
    driver.get(url)
    driver.find_element_by_id('J_Quick2Static').click()
    driver.find_element_by_id('TPL_username_1').clear()
    time.sleep(1)
    driver.find_element_by_id('TPL_username_1').send_keys('账号')
    time.sleep(2)
    driver.find_element_by_id('TPL_password_1').send_keys('密码')
    driver.find_element_by_id('J_SubmitStatic').click()
    # 需要滑块，再次登录，先输入密码，再滑动滑块
    driver.find_element_by_id("TPL_password_1").click() 
    driver.find_element_by_id("TPL_password_1").send_keys('密码')
    time.sleep(1)
    dragger = driver.find_element_by_id('nc_1_n1z')  # .滑块定位
    action = ActionChains(driver)
    for index in range(500):
        try:
            action.drag_and_drop_by_offset(dragger, 500, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
        except Exception:
            break
        time.sleep(11)

    driver.find_element_by_id('J_SubmitStatic').click()  # 重新摁登录摁扭

