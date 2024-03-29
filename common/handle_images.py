import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import cv2
import base_path
import os
from common.basepage import remover_activity_bar


def take_screenshot(url, file_path, lock):
    """
    :param url:
    :param file_path:
    :param lock:
    :return:
    """
    # 设置Chrome选项，运行在无界面模式（无GUI）
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        # 打开网页并保存截图
        driver.set_window_size(1920, 1080)  # 设置窗口大小为1920x1080像素
        driver.get(url)
        remover_activity_bar(driver)

        with lock:
            driver.save_screenshot(file_path)
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


def main(item, page_img_dir):
    pre_environment_url = item['pre_url']
    online_environment_url = item['pro_url']

    pre_screenshot_path = os.path.join(page_img_dir, item['page_type'])
    online_screenshot_path = os.path.join(page_img_dir, item['page_type'])
    diff_image_path = os.path.join(page_img_dir, item['page_type'])

    # 创建文件夹
    list_path = [pre_screenshot_path, online_screenshot_path, diff_image_path]
    for paths in list_path:
        if not os.path.exists(paths):
            os.makedirs(paths)

    pre_screenshot_path = os.path.join(page_img_dir, item['page_type'], item['page_name'] + "_pre.png")
    online_screenshot_path = os.path.join(page_img_dir, item['page_type'], item['page_name'] + "_pro.png")
    diff_image_path = os.path.join(page_img_dir, item['page_type'], item['page_name'] + "_diff.png")

    # 创建锁对象
    lock = threading.Lock()

    # 创建两个线程，分别加载预发布和在线环境的截图
    thread1 = threading.Thread(target=take_screenshot, args=(pre_environment_url, pre_screenshot_path, lock))
    thread2 = threading.Thread(target=take_screenshot, args=(online_environment_url, online_screenshot_path, lock))

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待两个线程执行完毕
    thread1.join()
    thread2.join()

    # 读取图像
    pre_img = cv2.imread(pre_screenshot_path)
    online_img = cv2.imread(online_screenshot_path)

    # 比较图像
    is_similar = compare_images(pre_img, online_img)

    if is_similar:
        print("未发现视觉差异。")
    else:
        print(f"检测到页面差异,正在生成带标记的预览差异图像：PRE_URL=({pre_environment_url}),PRO_URL=({online_environment_url})")
        mark_differences(pre_img, online_img, diff_image_path)
        raise Exception()


if __name__ == "__main__":
    lock = threading.Lock()
    take_screenshot('https://www.azazie.com/all/sample-brides?sort_by=popularity&current_in_stock=yes','./ccc.png',lock)
