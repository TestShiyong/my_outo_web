import pytest

from common.webpage_screenshot_comparison import run_comparison
from pages import all_page_data
from pages.all_page_data import get_bd_datas
from pages.all_page_data import get_acc_datas


class TestPageComparison:

    # @pytest.mark.parametrize('page_data', get_acc_datas())
    # def test_compare_acc_list(self, page_data, skip_if_goods_number_zero):
    #     run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['base_path'],
    #                    page_data['pre_list_screenshots_path'],
    #                    page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
    #                    page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
    #                    page_data['detail_diff_image_path'], page_data['quick_shop'], page_data['goods_number']
    #                    )

    @pytest.mark.parametrize('page_data', get_bd_datas())
    def test_compare_acc_list(self, page_data):
        run_comparison(page_data['pro_url'], page_data['pre_url'], page_data['base_path'],
                       page_data['pre_list_screenshots_path'],
                       page_data['pre_detail_screenshots_path'], page_data['pro_list_screenshots_path'],
                       page_data['pro_detail_screenshots_path'], page_data['list_diff_image_path'],
                       page_data['detail_diff_image_path'], page_data['quick_shop']
                       )
