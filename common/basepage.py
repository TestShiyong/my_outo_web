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

    def switch_to_window(self, old=False):

        time.sleep(2)
        win_s = self.driver.window_handles
        try:
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

    def scroll_to_bottom(self):
        """
        将浏览器滚动到页面底部
        :param driver: WebDriver对象
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_random_commodity(self, random_number=None):
        all_commoditys = By.XPATH, '//a[@data-datalayer-category="PlusSizeGowns"]'
        if random_number:
            rd = random_number
            self.scroll_to_bottom()
            self.close_new_user_pop()
            self.click_element(all_commoditys, '随机 点击BD列表页商品', rd)
        else:
            rd = random.randint(0, 60)
            self.scroll_to_bottom()
            self.click_element(all_commoditys, '随机 点击BD列表页商品', rd)

    def scroll_to_element(self, element):
        """
        将浏览器滚动到特定元素位置
        :param driver: WebDriver对象
        :param element: 要滚动到的元素
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def close_new_user_pop(self, loc=None):
        loc = loc if loc else By.XPATH, '//button[@aria-label="Close button"]'

        self.click_element(loc, '关闭新客弹窗')


if __name__ == '__main__':
    pass
