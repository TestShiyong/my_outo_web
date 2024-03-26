#:@ TIME 2021/12/6   0:20
#:@FILE  action_xiala.py
#:@EMAIL  1557225637@QQ.COM
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.baidu.com/')

wait = WebDriverWait(driver, 20)
elc = (By.XPATH, "//span[@id=\"s-usersetting-top\"]")
wait.until(EC.visibility_of_element_located(elc))
# 获取要移动的元素对象
ele = driver.find_element(*elc)
# 创建鼠标对象
mouse = ActionChains(driver)
# 移动到指定对象 保存
mouse.move_to_element(ele).perform()

elc2 = (By.XPATH, '//a[@class="setpref"]')
wait.until(EC.visibility_of_element_located(elc))
driver.find_element(*elc2).click()

driver.find_element(By.XPATH, '//li[text()="高级搜索"]').click()

driver.find_element(By.XPATH, '//div[@class="c-select-dropdown adv-ft-dropdown"]/preceding-sibling::div').click()

driver.find_element(By.XPATH, '//p[@data-value="rtf"]').click()
