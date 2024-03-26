#:@ TIME 2021/12/1   19:40
#:@FILE  js.py
#:@EMAIL  1557225637@QQ.COM
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待类  传入driver 和最大等待时间  和条件
from selenium.webdriver.support import expected_conditions as EC  # 条件  模块直接用类引用类方法 作为条件

'''
presence_of_element_located:元素存在
visibility_of_element_located:元素可见
element_to_be_clickable:元素可点击

'''

# 创建driver对象
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()


# 等待封装
def waite(driver, element):
    # 创建waite 对象传入 driver 最大等待时间
    wait = WebDriverWait(driver, 20)
    # wait对象调用until方法，传入 EC.(元素条件（元素表达式）)
    wait.until(EC.visibility_of_element_located(element))


# #已知元素id  js定位方法
# js="a=document.getElementById(\"train_date\");" \
#    "a.readOnly=false;" \
#    "a.value=\"2021-11-15\""
# driver.execute_script(js)

# 访问链接
driver.get('https://www.azazie.com/')
els = driver.find_element(By.ID, 'subscribe_email').send_keys("输入")

# 不知元素id js定位方法
js1 = "arguments[0].value=\"2021-11-15\""
driver.execute_script(js1, els)
