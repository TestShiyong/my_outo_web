#:@ TIME 2021/12/3   0:42
#:@FILE  window_handle.py
#:@EMAIL  1557225637@QQ.COM
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def waite(driver, element):
    waite = WebDriverWait(driver, 5)
    waite.until(expected_conditions.visibility_of_element_located(element))


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(5)

driver.get('https://www.baidu.com/')

driver.find_element(By.ID, 'kw').send_keys('selenium')

driver.find_element(By.ID, 'su').click()
time.sleep(1)

driver.find_element(By.XPATH, '//h3[@class="t c-title-en"]//a').click()
# 获取网页所有窗口句柄
win_handle = driver.window_handles

print('打印当前句柄：{}'.format(driver.current_window_handle))

print(win_handle)
# 切换到指定句柄
driver.switch_to.window(win_handle[1])

time.sleep(1)

element = (By.XPATH, '//a[@class="selenium-button selenium-webdriver text-uppercase font-weight-bold"]')

driver.find_element(*element).click()

time.sleep(2)

driver.close()

time.sleep(3)

driver.quit()
