#:@ TIME 2021/12/24   17:54
#:@FILE  basepage.py
#:@EMAIL  1557225637@QQ.COM
from common.handle_log import logg as log
from base_path import error_picture_dir
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random


class BasePage:
    '''
    def waite_ele_visible：封装的等待元素可见方法 #打印-计时-try-等待-expect-打印-截图-r-else打印等待时长

    def get_element(self,loc,page_action): 封装的 find 元素方法 ，打印-调用封装好的等待-try-查找元素-expect  打印失败-截图-raise-else-return 元素


    '''

    def __init__(self, drever: WebDriver):
        self.driver = drever

    def __waite_ele_visible(self, loc, page_action=None, time_out=20):
        if page_action:
            log.info('在 {} 行为,等待元素：{} 可见'.format(page_action, loc))
        # 等待开始时间
        start = time.time()
        # 捕捉异常
        try:
            WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(loc))
        except Exception as error:
            log.exception(f"等待({loc})元素可见失败")
            self.get_page_img(page_action)
            raise error
        else:
            end = time.time()
            log.info(f'等待元素({loc})成功，等待时间为:{start - end}')

    def get_element(self, loc, page_action=None, index=None, ):
        self.__waite_ele_visible(loc, page_action)
        if page_action:
            log.info('在  {}  行为,查找元素：{}'.format(page_action, loc))
        if index:
            try:
                loc_obj = self.driver.find_elements(*loc)[index]
            except Exception as error:
                log.info("查找:{} 元素失败".format(loc))
                self.get_page_img(page_action)
                raise error
            else:
                return loc_obj
        else:
            try:
                loc_obj = self.driver.find_element(*loc)
            except Exception as error:
                log.exception("查找:{} 元素失败".format(loc))
                self.get_page_img(page_action)
                raise error
            else:
                return loc_obj

    def click_element(self, loc, page_action=None, index=None):
        if page_action:
            log.info('在 {} 行为,点击元素：{}'.format(page_action, loc))
        loc_obj = self.get_element(loc, page_action, index)
        try:
            loc_obj.click()
        except Exception as error:
            log.exception("点击元素失败")
            self.get_page_img(page_action)
            raise error

    def input_value(self, loc, value, page_action=None, index=None, submit=False):
        loc_obj = self.get_element(loc, page_action, index)
        try:
            if page_action:
                log.info('在 {} 行为，操作input元素：{}'.format(page_action, loc))
            loc_obj.send_keys(value)
            if submit:
                loc_obj.send_keys(Keys.ENTER)
        except:
            log.exception('输入文本失败')
            self.get_page_img(page_action)
            raise

        else:
            log.info('value 输入成功,value为：{}'.format(value))

    def get_text(self, loc, page_action=None, index=None):

        loc_obj = self.get_element(loc, page_action, index)
        try:
            if page_action == '':
                log.info('在 {} 行为，获取元素文本:{}'.format(page_action, loc))
            text_obj = loc_obj.text
        except:
            log.exception('获取文本失败')
            self.get_page_img(page_action)
            raise
        else:
            log.info('获取文本元素成功，元素为：{}'.format(text_obj))
            return text_obj

    def get_page_img(self, page_action):
        # 命名规范 XX页面XX操作XX截图时间

        # 当前时间
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # 文件名称
        file_path = os.path.join(error_picture_dir, '{}_{}.png'.format(page_action, current_time))
        # 调用截图方法 传入文件路径
        self.driver.save_screenshot(file_path)

    def swich_to_window(self, old=False):

        time.sleep(2)

        log.info('获取当前 浏览器所有窗口句柄')
        win_s = self.driver.window_handles
        try:
            log.info('准备切换到最新窗口')
            if old:
                self.driver.switch_to.window(win_s[0])
            else:
                self.driver.switch_to.window(win_s[-1])
        except:
            log.exception('切换到新窗口失败')
        else:
            log.info('成功切换到新窗口')

    def remover_activity_bar(self):
        activity_bar_loc = By.ID, 'activity_bar'
        try:
            element_remove_bar = self.driver.find_element(*activity_bar_loc)
            self.driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element_remove_bar)
        except NoSuchElementException:
            print("未找到指定元素 activity_bar")

    def click_random_commodity(self):
        all_commoditys = By.XPATH, '//a[@data-datalayer-category="PlusSizeGowns"]'
        rd = random.randint(0, 60)
        self.click_element(all_commoditys, '随机 点击BD列表页商品', rd)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    new_basepage = Base_page(driver)
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    loc = (By.ID, 'kw')
    new_basepage.input_value(loc, '百度输入框输入文本', '柠檬班')
