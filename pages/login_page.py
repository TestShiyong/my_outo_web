#:@ TIME 2021/12/20   15:52
#:@FILE  login_page.py
#:@EMAIL  1557225637@QQ.COM
from selenium.webdriver.common.by import By
from common.basepage import BasePage


# login页对象类
class LoginPage(BasePage):
    # 用户名输入框
    input_email_elm = By.ID, '_email'
    # 密码输入框
    input_password_elm = By.ID, '_password'
    # 登录按钮
    login_button_elm = By.XPATH, '//button[@tabindex="4"]'

    # Please enter an email address.
    empty_user = By.XPATH, '//span[@class="waiting"]/following-sibling::span'
    # Please enter your password.
    empty_password = By.XPATH, '//input[@id="_password"]/following::span'
    # Please enter a valid email.
    invalid_email = By.XPATH, '//span[@class="waiting"]/following-sibling::span'
    # The email address or password you entered is incorrect.
    password_error = By.XPATH, '//span[@class="help-block"]'

    # 登录成功功能
    def login(self, email, password):
        # login
        self.input_value(self.input_email_elm, '输入email', email)
        self.input_value(self.input_password_elm, '输入密码', password)
        self.click_element(self.login_button_elm, '点击登录')

    # def get_all_data_empty_msg(self):
    #     return self.get_text(lg.empty_user,'全部参数为空')
    #
    # def get_emial_empty(self):
    #     return self.get_text(lg.empty_user,'用户名为空')
    #
    # def get_password_empty(self):
    #     return self.get_text(lg.empty_password,'为空的密码')
    #
    # def get_invalid_email(self):
    #     return self.get_text(lg.invalid_email,'无效的email')
    # def
