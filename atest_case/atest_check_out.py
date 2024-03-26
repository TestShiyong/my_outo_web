#:@ TIME 2022/1/2   10:27
#:@FILE  test_check_out.py
#:@EMAIL  1557225637@QQ.COM
import pytest
from pages.list_page_bridesmaids import ListPageBridesmaids as BD
from pages.home_page import HomePage


class Test_check_out:
    @pytest.mark.mark1
    @pytest.mark.usefixtures('init_fixture')
    def test_check_out_bd(self, init_fixture):
        HomePage(init_fixture).click_navigation_BD()
        BD(init_fixture).click_random_commodity()
