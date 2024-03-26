from selenium import webdriver
from selenium.webdriver.common.by import By

option_driver = webdriver.ChromeOptions()
# option_driver.add_argument('--headless')
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get('https://www.azazie.com/')

activity_bar_loc = By.ID, 'activity_bar'
element_remove_bar = driver.find_element(*activity_bar_loc)
driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element_remove_bar)
input("Press Enter to close the browser...")
