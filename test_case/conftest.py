# #:@ TIME 2021/12/20   0:01
# #:@FILE  conftest.py
# #:@EMAIL  1557225637@QQ.COM
import pytest
import time


# from common.log import logg
#
# from common.log import logg
#
# from selenium import webdriver
#
#
# #@pytest.fixture(scope='class')
# @pytest.fixture()
# def init_fixture():
#     logg.info("==========   class级  前置条件：打开Chrome浏览器，访问登录页面    ==========")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.azazie.com")
#     time.sleep(2)
#     yield driver
#     logg.info("==========   class级  后置条件：关闭浏览器    ==========")
#     driver.quit()
#
#
# @pytest.fixture
# def back_login_page(init_fixture):
#     logg.info('==========   function级   前置条件：刷新浏览器')
#     init_fixture.get('https://www.azazie.com/user/login')
#
#     yield init_fixture
#
#

@pytest.fixture
def skip_if_goods_number_zero(page_data):
    if page_data['goods_number'] == 0:
        pytest.skip("Skipping test because goods_number is 0")


if __name__ == '__main__':
    pass
