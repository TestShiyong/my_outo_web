from selenium import webdriver

# 启动浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.example.com")

# 执行JavaScript来滚动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
