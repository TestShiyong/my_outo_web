#:@ TIME 2021/11/28   23:07
#:@FILE  web_iframe.py
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


# 访问链接
driver.get('https://ke.qq.com/')
time.sleep(2)
driver.implicitly_wait(5)

# #创建等待对象
# wait=WebDriverWait(driver,20)
# 元素表达
ele = (By.ID, 'js_login')
# 显示等待
waite(driver, ele)
# 点击登录按钮
driver.find_element(*ele).click()
# #iframe无属性 通过下标获取iframe
# iframe=driver.find_elements(By.TAG_NAME,'iframe')[2]
# driver.switch_to.frame(iframe)

# #iframe无属性 通过元素定位返回iframe
iframe = driver.find_element(By.XPATH, '//iframe[@width="368px"]')
# 切换到iframe
driver.switch_to.frame(iframe)

waite(driver, (By.ID, 'switcher_plogin'))

# 点击账号密码登录
driver.find_element(By.ID, 'switcher_plogin').click()
# 退回到初始html页
driver.switch_to.default_content()

driver.find_element(By.XPATH, '//a[@class="login-close"]//i[@class="icon-font i-close"]').click()
# 强制等待
# time.sleep(3)
# #关闭浏览器
# driver.quit()

# 相对路径用法
'''
1.//标签名[@属性名=值]
2.//标签名[tetx()=值]
3.//标签名[contains(@属性名,值)  //标签名[contains(tetx(),值)]

组合条件
逻辑 and 与 or
//a[@href="/all/wedding-dresses" and @class="nav-a-link"]
//    
'''
