import time

import base_path
from pages import all_page_url
from common.handle_images import main

screenshots_dir = base_path.page_screenshots_dir


#
#
# def test_compare_bd_list():
#     page_date = all_page_url.get_bd_urls()
#     for item in page_date:
#         main(item, screenshots_dir)
#
#
# def test_compare_jbd_list():
#     page_date = all_page_url.get_jbd_urls()
#     for item in page_date:
#         main(item, screenshots_dir)
#
#
# def test_compare_sod_list():
#     page_date = all_page_url.get_sod_urls()
#     for item in page_date:
#         main(item, screenshots_dir)
#
#
# def test_compare_acc_list():
#     page_date = all_page_url.get_acc_urls()
#     for item in page_date:
#         main(item, screenshots_dir)


def test_compare_sample_list():
    page_date = all_page_url.get_sample_urls()
    for item in page_date:
        main(item, screenshots_dir)


# def test_compare_swatch_list():
#     page_date = all_page_url.get_swatch_urls()
#     for item in page_date:
#         main(item, screenshots_dir)
#
#
# def test_compare_rts_list():
#     page_date = all_page_url.get_rts_urls()
#     for item in page_date:
#         main(item, screenshots_dir)

#
#



