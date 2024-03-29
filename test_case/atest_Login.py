#:@ TIME 2021/12/20   0:00
#:@FILE  test_Login.py
#:@EMAIL  1557225637@QQ.C
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time
from case_data import login_data as dt
from common.handle_log import logg

import pytest


# 调用fixture  方法级别前置方法 嵌套的类级别
@pytest.mark.usefixtures('back_login_page')
class Test_login:
    logg.info('开始执行login 用例')

    def test_all_data_empty(self, back_login_page):
        # 创建 login页对象传入fixture返回的driver 调用登录方法
        LoginPage(back_login_page).login(*dt.all_data_empty['data'])
        assert back_login_page.find_element(*LoginPage.empty_user).text in dt.all_data_empty['expect']

    def test_emial_empty(self, back_login_page):
        # 创建 login页对象传入fixture返回的driver 调用登录方法
        LoginPage(back_login_page).login(*dt.emial_empty['data'])
        assert back_login_page.find_element(*LoginPage.empty_user).text in dt.emial_empty['expect']

    def test_password_empty(self, back_login_page):
        # 创建 login页对象传入fixture返回的driver 调用登录方法
        LoginPage(back_login_page).login(*dt.password_empty['data'])
        assert back_login_page.find_element(*LoginPage.empty_password).text in dt.password_empty['expect']

    def test_invalid_email(self, back_login_page):
        # 创建 login页对象传入fixture返回的driver 调用登录方法
        LoginPage(back_login_page).login(*dt.invalid_email['data'])
        assert back_login_page.find_element(*LoginPage.invalid_email).text in dt.invalid_email['expect']

    def test_error_password(self, back_login_page):
        # 创建 login页对象传入fixture返回的driver 调用登录方法
        LoginPage(back_login_page).login(*dt.error_password['data'])
        time.sleep(2)
        assert back_login_page.find_element(*LoginPage.password_error).text in dt.error_password['expect']

    # 传入fixture 返回的driver
    def test_login(self, back_login_page):
        # 创建login页对象 调用Login页 login方法
        LoginPage(back_login_page).login(*dt.user_data)
        # 创建首页对象 调用获取用户名方法  做断言
        assert HomePage(back_login_page).expect_login_succeed() != 'Sign In'
