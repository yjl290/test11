# coding=utf-8

import time

from selenium import webdriver
from Util.Simulate_Mouse import Simulate_Mouse

driver = webdriver.Chrome()  # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()

driver.maximize_window()  # 最大化浏览器窗口

driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://jiaoyanpre.lexue.com/")  # 地址栏输入百度地址

driver.find_element_by_xpath("//*[@id='normal_login_email']").send_keys("yangjunlin@lexue.com")  #输入账号
driver.find_element_by_xpath("//*[@id='normal_login_pass']").send_keys(".014789+")#输入账号
driver.find_element_by_xpath("//*[@id='normal_login_remember']").click()#记住我
#time.sleep(2)
driver.find_element_by_xpath("//*[@id='normal_login_remember']").click()#记住我
driver.find_element_by_xpath("//*[@id='form_box___1vHVT']/form/div[3]/div/div/span/span/span").click()#点击年级学段
# 点击百度一下按钮
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul[1]/li[4]").click()#点击学段
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul[2]/li[1]").click()#点击学科

#time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_box___1vHVT']/form/div[4]/div/div/span/button").click()#点击登录

# 导入time模块，等待2秒

# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。

# 这里采用了相对元素定位方法/../

# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。

#driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()


userElement = driver.find_element_by_xpath("//*[@id='username___3b9qc']/li[2]/div/span")
print(userElement.text)

Simulate_Mouse(driver).move_mouse(userElement)#鼠标悬停
time.sleep(3)
#subjectElement = driver.find_element_by_xpath("//*[@id='4$Menu']/li[1]")
subjectElement = driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[1]")
print(subjectElement.text)
#print(driver.find_element_by_xpath("/html/body/div[7]/div/div/ul/li[2]").text)
print(driver.find_element_by_xpath("//*[@id='4$Menu']/li[2]").text)
print(driver.find_element_by_xpath("//*[@id='4$Menu']/li[3]").text)

#print(driver.find_element_by_xpath("/html/body/div[7]/div/div/ul/li[3]").text)

Simulate_Mouse(driver).move_mouse(userElement)
driver.find_element_by_xpath("//*[@id='4$Menu']/li[2]").click()  #修改密码
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/button").click()

Simulate_Mouse(driver).move_mouse(userElement)
driver.find_element_by_xpath("//*[@id='4$Menu']/li[2]").click()  #修改密码
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/span/input").send_keys("y.014789+")
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[3]/span/input").send_keys(".014789+")
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[4]/span/input").send_keys(".014789+")
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[5]/button").click()


driver.find_element_by_xpath("//*[@id='normal_login_email']").send_keys("yangjunlin@lexue.com")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='normal_login_pass']").send_keys("y.014789+")
driver.find_element_by_xpath("//*[@id='normal_login_remember']").click()
#time.sleep(2)
driver.find_element_by_xpath("//*[@id='normal_login_remember']").click()
driver.find_element_by_xpath("//*[@id='form_box___1vHVT']/form/div[3]/div/div/span/span/span").click()
# 点击百度一下按钮
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul[1]/li[4]").click()
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul[2]/li[1]").click()

#time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_box___1vHVT']/form/div[4]/div/div/span/button").click()
Simulate_Mouse(driver).move_mouse(userElement)
driver.find_element_by_xpath("//*[@id='4$Menu']/li[3]").click()  #退出
time.sleep(3)
driver.quit()
