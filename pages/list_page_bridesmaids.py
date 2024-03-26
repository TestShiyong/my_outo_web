#:@ TIME 2022/1/2   10:17
#:@FILE  list_page_bridesmaids.py
#:@EMAIL  1557225637@QQ.COM
from selenium.webdriver.common.by import By
from common.basepage import BasePage
import random


class ListPageBridesmaids(BasePage):
    all_commoditys = By.XPATH, '//a[@data-datalayer-category="PlusSizeGowns"]'

    def click_random_commodity(self):
        rd = random.randint(0, 60)
        # loc_obj=self.get_element(BD.all_commoditys,'随机 点击BD列表页商品',rd)

        self.click_element(self.all_commoditys, '随机 点击BD列表页商品', rd)
