import time

import base_path
from pages import all_page_url
from common.handle_images import run_comparison

screenshots_path = base_path.screenshots_path



def test_compare_bd_list():
    list_page_dates = all_page_url.get_bd_urls()
    for page_date in list_page_dates:
        run_comparison(page_date['pro_url'], page_date['pre_url'], page_date['pre_list_screenshots_path'],
                       page_date['pre_detail_screenshots_path'], page_date['pro_list_screenshots_path'],
                       page_date['pro_detail_screenshots_path'], page_date['list_diff_image_path'],
                       page_date['detail_diff_image_path']
                       )

#
# def test_compare_jbd_list():
#     page_date = all_page_url.get_jbd_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
#
#
# def test_compare_sod_list():
#     page_date = all_page_url.get_sod_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
#
#
# def test_compare_acc_list():
#     page_date = all_page_url.get_acc_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
#
#
# def test_compare_sample_list():
#     page_date = all_page_url.get_sample_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
#
#
# def test_compare_swatch_list():
#     page_date = all_page_url.get_swatch_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
#
# def test_compare_rts_list():
#     page_date = all_page_url.get_rts_urls()
#     run_comparison(page_date['page_name'], page_date['pro_url'], page_date['pre_url'], page_date['page_type'],
#                    screenshots_path)
