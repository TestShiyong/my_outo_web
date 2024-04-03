import time

import pytest
import base_path
from common.basepage import BasePage
from pages import all_page_url as al_page
from common.handle_images import run_comparison


class TestPageComparison:
    screenshots_path = base_path.screenshots_path

    @pytest.mark.parametrize('page_data', al_page.get_bd_urls())
    def test_compare_bd_list(self, page_data):
        try:
            run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
                           page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
                           page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
                           page_data['detail_diff_image_path']
                           )
        except Exception as e:
            print("Exception occurred:", e)

    # @pytest.mark.parametrize('page_data', al_page.get_jbd_urls())
    # def test_compare_jbd_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
    #
    #
    # @pytest.mark.parametrize('page_data', al_page.get_sod_urls())
    # def test_compare_sod_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
    #
    #
    # @pytest.mark.parametrize('page_data', al_page.get_acc_urls())
    # def test_compare_acc_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
    #
    #
    # @pytest.mark.parametrize('page_data', al_page.get_sample_urls())
    # def test_compare_sample_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
    #
    #
    # @pytest.mark.parametrize('page_data', al_page.get_swatch_urls())
    # def test_compare_swatch_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
    #
    #
    # @pytest.mark.parametrize('page_data', al_page.get_rts_urls())
    # def test_compare_rts_list(page_data):
    #     try:
    #         run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['pre_list_screenshots_path'],
    #                        page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                        page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                        page_data['detail_diff_image_path']
    #                        )
    #     except Exception as e:
    #         print("Exception occurred:", e)
