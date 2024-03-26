#:@ TIME 2021/12/3   2:14
#:@FILE  daka.py
#:@EMAIL  1557225637@QQ.COM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from threading import Timer


def waite(driver, ele):
    waite = WebDriverWait(driver, 10)
    waite.until(expected_conditions.visibility_of_element_located(ele))


def daka():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.implicitly_wait(5)

    driver.get('https://oc.gaoyaya.com/')

    driver.find_element(By.ID, 'username').send_keys('shiyong')
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys('shi979796.')
    driver.find_element(By.ID, 'subReal').click()

    time.sleep(5)

    driver.find_element(By.XPATH, '//div[@class="clock-in-circle"]').click()

    time.sleep(2)


daka()
