#:@ TIME 2021/12/3   1:44
#:@FILE  tanchuang.py
#:@EMAIL  1557225637@QQ.COM
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


def waite(driver, elc):
    waite = WebDriverWait(driver, 5)
    waite.until(expected_conditions.visibility_of_element_located(elc))


# driver=webdriver.Chrome()

# 处理提示消息弹窗
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'notifications': 2
    }
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)

driver.get('https://www.azazie.com/')

driver.maximize_window()

elc = (By.XPATH, "//div[@class=\"first-open-btn\"]")
waite(driver, elc)
driver.find_element(*elc).click()

alter = driver.switch_to.alert

alter.accept()
