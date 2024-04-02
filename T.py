from selenium import webdriver
from common.basepage import BasePage
def scroll_to_element(driver, element):
    """
    将浏览器滚动到特定元素位置
    :param driver: WebDriver对象
    :param element: 要滚动到的元素
    """
    driver.execute_script("arguments[0].scrollIntoView();", element)

# 示例用法
if __name__ == "__main__":
    # 启动浏览器
    driver = webdriver.Chrome()

    # 打开网页
    driver.get("https://www.azazie.com")
    base_page = BasePage(driver)
    # 找到特定的元素
    base_page.scroll_to_bottom()
    base_page.close_new_user_pop()

