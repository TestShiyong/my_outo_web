import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import cv2
import base_path
import os
from common.basepage import BasePage


def take_screenshot(url, list_screenshot_path, detail_screenshot_path):
    """
    :param url:
    :param list_screenshot_path:
    :param detail_screenshot_path:
    :return:
    """
    # 设置Chrome选项，运行在无界面模式（无GUI）
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    base_page = BasePage(driver)

    try:
        # 打开网页并保存截图
        driver.set_window_size(1920, 1080)  # 设置窗口大小为1920x1080像素
        driver.get(url)
        base_page.remover_activity_bar()

        base_page.driver.save_screenshot(list_screenshot_path)
        base_page.click_random_commodity()
        base_page.driver.save_screenshot(detail_screenshot_path)

    finally:
        driver.quit()


def compare_images(pre_img, online_img, threshold=30):
    """
    判断两个图像是否相似
    :param pre_img:
    :param online_img:
    :param threshold:
    :return:
    """
    # 使用绝对差异找到不同之处
    diff = cv2.absdiff(pre_img, online_img)
    # 转换为灰度图像
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # 将灰度图像进行阈值化处理
    _, thresh = cv2.threshold(diff_gray, threshold, 255, cv2.THRESH_BINARY)
    # 输出可以用于绘制轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 判断两个图像是否相似
    is_similar = len(contours) == 0
    return is_similar


def mark_differences(pre_img, online_img, diff_image_path, threshold=30):
    # 使用绝对差异找到不同之处
    diff = cv2.absdiff(pre_img, online_img)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(diff_gray, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 在pre_img上绘制标记差异的矩形
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(pre_img, (x, y), (x + w, y + h), (255, 0, 0), 1)

    # 将pre_img和online_img合并成单个图像
    combined_img = Image.new('RGB', (pre_img.shape[1] * 2, pre_img.shape[0]))
    combined_img.paste(Image.fromarray(pre_img), (0, 0))
    combined_img.paste(Image.fromarray(online_img), (pre_img.shape[1], 0))

    combined_img.save(diff_image_path)


def run_comparison(page_name, pro_url, pre_url, page_type, screenshots_path):
    pre_screenshot_path = os.path.join(screenshots_path, page_type)
    online_screenshot_path = os.path.join(screenshots_path, page_type)
    diff_image_path = os.path.join(screenshots_path, page_type)

    list_path = [pre_screenshot_path, online_screenshot_path, diff_image_path]
    for paths in list_path:
        if not os.path.exists(paths):
            os.makedirs(paths)

    pre_path = os.path.join(screenshots_path, page_type, page_name + "_pre.png")
    pro_path = os.path.join(screenshots_path, page_type, page_name + "_pro.png")
    diff_image_path = os.path.join(screenshots_path, page_type, page_name + "_diff.png")

    # 创建两个线程，分别加载预发布和在线环境的截图
    thread1 = threading.Thread(target=take_screenshot, args=(pre_url, pre_path))
    thread2 = threading.Thread(target=take_screenshot, args=(pro_url, pro_path))

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待两个线程执行完毕
    thread1.join()
    thread2.join()

    # 读取图像
    pre_img = cv2.imread(pre_path)
    pro_img = cv2.imread(pro_path)

    # 比较图像
    is_similar = compare_images(pre_img, pro_img)

    if is_similar:
        print("未发现视觉差异。")
    else:
        print(f"检测到页面差异,正在生成带标记的预览差异图像：PRE_URL=({pre_url}),PRO_URL=({pro_url})")
        mark_differences(pre_img, pro_img, diff_image_path)


# 示例用法
if __name__ == "__main__":
    item = {
        'pre_url': 'https://www.example.com/pre',
        'pro_url': 'https://www.example.com/pro',
        'page_type': 'example_page',
        'page_name': 'example_page_name'
    }
    screenshots_path = 'screenshot'
    run_comparison(item, screenshots_path)
