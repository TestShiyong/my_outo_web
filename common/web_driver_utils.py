from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time


def perform_mouse_hover():
    """
    driver鼠标悬浮操作
    :return:
    """
    # 初始化 WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')

    # 定位元素
    loc = (By.XPATH, "//span[@id=\"s-usersetting-top\"]")
    element = driver.find_element(*loc)

    # 创建鼠标动作对象
    mouse_actions = ActionChains(driver)

    # 执行鼠标悬停动作
    mouse_actions.move_to_element(element).perform()

    # 等待一段时间
    time.sleep(10)


def handle_alert():
    """
    弹窗处理
        alert = driver.switch_to.alert
        alert.accept()
    :return:
    """
    # 创建 WebDriver 实例
    driver = webdriver.Chrome()
    # 打开网页
    driver.get("https://www.example.com")

    try:
        # 尝试捕获弹窗
        alert = driver.switch_to.alert

        # 获取弹窗文本内容
        alert_text = alert.text
        print("弹窗内容：", alert_text)

        # 可以选择接受、拒绝或者输入内容等
        # 例如，接受弹窗
        alert.accept()

    except:
        # 如果没有找到弹窗，可以在此处处理异常
        print("未发现弹窗")
    # 关闭浏览器
    driver.quit()


def remove_page_element(driver, loc):
    """
    移除页面元素
    :param driver:
    :param loc:
    :return:
    """
    activity_bar_loc = By.ID, 'activity_bar'
    element_remove_bar = driver.find_element(*activity_bar_loc)
    driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element_remove_bar)


def switch_to_iframe(driver, iframe_locator):
    try:
        # 切换到 iframe
        iframe = driver.find_element(*iframe_locator)
        driver.switch_to.frame(iframe)
        print("切换到 iframe 成功")

    except:
        print("未找到 iframe 或切换失败")


def switch_to_window(driver, window_number):
    try:
        # 获取当前所有窗口句柄
        handles = driver.window_handles

        # 切换到指定窗口
        driver.switch_to.window(handles[window_number])
        print("切换到窗口成功")

    except:
        print("窗口切换失败")


def scroll_to_bottom(driver):
    try:
        # 执行 JavaScript 滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("已滚动到页面底部")

    except:
        print("滚动失败")


def test_driver_wait(driver, loc):
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # 可见
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
    # 可点击
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc))
    # 存在
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc))
