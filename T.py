import time
import logging

import base_path
from pages import all_page_url
from common.handle_images import run_comparison

screenshots_dir = base_path.page_screenshots_dir

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_comparison_for_page(page_data):
    try:
        run_comparison(page_data, screenshots_dir)
    except Exception as e:
        logger.error(f"对比页面 {page_data['page_type']} 时出现错误: {str(e)}")


def test_compare_pages(compare_function, page_name):
    logger.info(f"开始对比 {page_name} 页面...")
    page_data = compare_function()
    for item in page_data:
        run_comparison_for_page(item)
    logger.info(f"{page_name} 页面对比完成。")


def test_compare_bd_list():
    test_compare_pages(all_page_url.get_bd_urls, "BD")


def test_compare_jbd_list():
    test_compare_pages(all_page_url.get_jbd_urls, "JBD")


def test_compare_sod_list():
    test_compare_pages(all_page_url.get_sod_urls, "SOD")


def test_compare_acc_list():
    test_compare_pages(all_page_url.get_acc_urls, "ACC")


def test_compare_sample_list():
    test_compare_pages(all_page_url.get_sample_urls, "SAMPLE")


def test_compare_swatch_list():
    test_compare_pages(all_page_url.get_swatch_urls, "SWATCH")


def test_compare_rts_list():
    test_compare_pages(all_page_url.get_rts_urls, "RTS")
