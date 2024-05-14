import time
import threading
from selenium import webdriver
from PIL import Image
import cv2
from common.basepage import BasePage
import random


def create_driver(is_headers=False):
    options = webdriver.ChromeOptions()
    if not is_headers:
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
    else:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    return driver


def take_screenshot(url, list_screenshot_path, base_path, detail_screenshot_path, random_number, quick_shop):
    """
    进入列表页截图 然后进入详情页截图
    :param url:
    :param list_screenshot_path:
    :param detail_screenshot_path:
    :param random_number:
    :return:
    """

    base_page = BasePage(create_driver())
    base_page.driver.get(url)
    base_page.driver.implicitly_wait(5)
    base_page.remover_activity_bar()
    base_page.save_screenshot(base_path, list_screenshot_path)
    base_page.click_random_commodity(quick_shop, '随机点击商品', random_index=random_number)
    base_page.switch_to_window()
    base_page.remover_activity_bar()
    base_page.driver.execute_script("document.body.style.zoom='67%'")  # 80% 的缩放比例
    base_page.save_screenshot(base_path, detail_screenshot_path)


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


def run_comparison(pro_url, pre_url, base_path, pre_list_screenshots_path, pre_detail_screenshots_path,
                   pro_list_screenshots_path, pro_detail_screenshots_path, list_diff_image_path, detail_diff_image_path,
                   quick_shop, goods_number=None):
    """
    多线程 调用对比方法
    :param pro_url:
    :param pre_url:
    :param base_path:
    :param pre_list_screenshots_path:
    :param pre_detail_screenshots_path:
    :param pro_list_screenshots_path:
    :param pro_detail_screenshots_path:
    :param list_diff_image_path:
    :param detail_diff_image_path:
    :param quick_shop:
    :param goods_number:
    :return:
    """
    # 设置Chrome选项，运行在无界面模式（无GUI）
    random_number = random.randint(1, 60) if not goods_number else random.randint(1, goods_number)
    # 创建两个线程，分别加载预发布和在线环境的截图
    thread1 = threading.Thread(target=take_screenshot,
                               args=(pre_url, pre_list_screenshots_path, base_path, pre_detail_screenshots_path,
                                     random_number, quick_shop))

    thread2 = threading.Thread(target=take_screenshot,
                               args=(pro_url, pro_list_screenshots_path, base_path, pro_detail_screenshots_path,
                                     random_number, quick_shop))

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待两个线程执行完毕
    thread1.join()
    thread2.join()

    # 读取图像
    pre_list_img = cv2.imread(pre_list_screenshots_path)
    pre_detail_img = cv2.imread(pre_detail_screenshots_path)
    pro_list_img = cv2.imread(pro_list_screenshots_path)
    pro_detail_img = cv2.imread(pro_detail_screenshots_path)

    # 比较图像
    list_is_similar = compare_images(pre_list_img, pro_list_img)
    detail_is_similar = compare_images(pre_detail_img, pro_detail_img)

    if list_is_similar:
        print("列表页截图对比未发现视觉差异。")
    else:
        print(f"检测到列表页面差异,正在生成带标记的预览差异图像：PRE_URL=({pre_url}),PRO_URL=({pro_url})")
        mark_differences(pre_list_img, pro_list_img, list_diff_image_path)
    if detail_is_similar:
        print("详情页截图对比未发现视觉差异。")
    else:
        print(f"检测到详情页面差异,正在生成带标记的预览差异图像：PRE_URL=({pre_url}),PRO_URL=({pro_url})")
        mark_differences(pre_detail_img, pro_detail_img, detail_diff_image_path)


# 示例用法
if __name__ == "__main__":
    pass
