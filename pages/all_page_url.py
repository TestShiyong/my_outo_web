from common.handle_red_conf_file import cf
from base_path import screenshots_path
import os

PRO_BASE_URL = cf.get_str('URL', 'PRO_BASE_URL')
PRE_BASE_URL = cf.get_str('URL', 'PRE_BASE_URL')

custom_p_number = 1
custom_pre_url = f'https://p{custom_p_number}.azazie.com'
BD_PAGES = {'list_page_bd_url': '/all/bridesmaid-dresses',
            'list_page_bd_plus_size_url': '/all/plus-size-bridesmaid-dresses',
            'list_page_maternity_url': '/all/maternity-bridesmaid-dresses',
            'list_page_modest_url': '/all/modest-bridesmaid-dresses'}

# MOB
MOB_PAGES = {'list_page_mother_url': '/all/mother-of-the-bride-dresses',
             'list_page_plus_sie_mob_url': '/all/plus-size-mother-of-the-bride-dresses'}

JBD_PAGES = {'list_page_all_jbd_url': '/all/all-junior',
             'list_page_junior_url': '/all/junior-bridesmaid-dresses',
             'list_page_flower_url': '/all/flower-girl-dresses'}

SOD_PAGES = {'list_page_sod_url': '/all/atelier-dresses'}

ACC_PAGES = {'list_page_all_acc_url': '/all/accessories',
             'list_page_groomsmen_rul': '/all/groomsmen-accessories',
             'list_page_shoes_url': '/all/shoes',
             'list_page_jewelry_url': '/all/jewelry',
             'list_page_headpieces': '/all/headpieces',
             'list_page_shapewear': '/all/shapewear',
             'list_page_wraps': '/all/wraps',
             'list_page_wedding_veils': '/all/wedding-veils',
             'list_page_sashes': '/all/sashes',
             'list_page_robes': '/all/robes',
             'list_page_gifts': '/all/gifts',
             'list_page_separates': '/all/separates',
             'list_page_garment_bags': '/all/garment-bags'}

SAMPLE_PAGES = {
    # 'list_page_all_sample_url': '/all/sample-dresses?current_in_stock=yes',
    'list_page_wd_sample_url': '/all/sample-brides?current_in_stock=yes',
    'list_page_bd_sample_url': '/all/sample-bridesmaids?sort_by=popularity&current_in_stock=yes',
    'list_page_maternity_sample_url': 'sort_by=popularity&current_in_stock=yes',
    'list_page_modest_sample_url': '/all/sample-modest?sort_by=popularity&current_in_stock=yes',
    'list_page_mother_sample_url': '/all/sample-mother-of-the-bride?sort_by=popularity&current_in_stock=yes',
    'list_page_junior_sample_url': '/all/sample-junior-bridesmaid-dresses?sort_by=popularity&current_in_stock=yes'}

SWATCH_PAGES = {'list_page_swatch_fabric_url': '/swatches-fabric',
                'list_page_swatches_url': '/all/swatches',
                'list_page_fabrics_url': '/all/fabrics'}

RTS_PAGES = {
    "list_page_all_rts_url": "/all/final-sale",
    "list_page_bd_rts_url": "/all/final-sale/with/category/ready-to-ship-bridesmaids?sort_by=popularity&current_in_stock=yes",
    "list_page_mob_rts_url": "/all/final-sale/with/category/ready-to-ship-mother-of-the-brides?sort_by=popularity&current_in_stock=yes",
    "list_page_wd_rts_url": "/all/final-sale/with/category/ready-to-ship-brides?sort_by=popularity&current_in_stock=yes",
    "list_page_sod_rts_url": "/all/final-sale/with/category/special-offer-special-occasion-dresses?sort_by=popularity&current_in_stock=yes",
    "list_page_flower_rts_url": "/all/final-sale/with/category/special-offer-flower-girl-dresses?sort_by=popularity&current_in_stock=yes",
    "list_page_junior_rts_url": "/all/final-sale/with/category/ready-to-ship-junior-bridesmaid-dresses?sort_by=popularity&current_in_stock=yes",
    "list_page_groomsmen_rts_url": "/all/final-sale/with/category/special-offer-groomsmen-accessories?sort_by=popularity&current_in_stock=yes",
    "list_page_maternity_rts_url": "/all/final-sale/with/category/ready-to-ship-maternity?sort_by=popularity&current_in_stock=yes",
    "list_page_modest_rts_url": "/all/final-sale/with/category/ready-to-ship-modest?sort_by=popularity&current_in_stock=yes",
    "list_page_shoes_rts_url": "/all/final-sale/with/category/special-offer-shoes?sort_by=popularity&current_in_stock=yes",
    "list_page_bags_rts_url": "/all/final-sale/with/category/special-offer-bags?sort_by=popularity&current_in_stock=yes",
    "list_page_jewelry_rts_url": "/all/final-sale/with/category/special-offer-jewelry?sort_by=popularity&current_in_stock=yes",
    "list_page_headpieces_rts_url": "/all/final-sale/with/category/special-offer-headpieces?sort_by=popularity&current_in_stock=yes",
    "list_page_shapewear_rts_url": "/all/final-sale/with/category/special-offer-shapewear?sort_by=popularity&current_in_stock=yes",
    "list_page_wrap_rts_url": "/all/final-sale/with/category/special-offer-wraps?sort_by=popularity&current_in_stock=yes",
    "list_page_veils_rts_url": "/all/final-sale/with/category/special-offer-wedding-veils?sort_by=popularity&current_in_stock=yes"

}


def handle_page_datas(pro_url, pre_url, page_items, cate_name):
    """

    :param pro_url:
    :param pre_url:
    :param page_items:
    :param cate_name:
    :return:
    """
    list_page_datas = []

    for name, url in page_items.items():
        pre_list_screenshots_path = os.path.join(screenshots_path, cate_name, name + "_list_pre.png")
        pre_detail_screenshots_path = os.path.join(screenshots_path, cate_name, name + "_detail_pre.png")
        pro_list_screenshots_path = os.path.join(screenshots_path, cate_name, name + "_list_pro.png")
        pro_detail_screenshots_path = os.path.join(screenshots_path, cate_name, name + "_detail_pro.png")
        list_diff_image_path = os.path.join(screenshots_path, cate_name, name + "_list_diff.png")
        detail_diff_image_path = os.path.join(screenshots_path, cate_name, name + "_detail_diff.png")

        list_page_datas.append({'pro_url': pro_url + url, 'pre_url': pre_url + url,
                                "pre_list_screenshots_path": pre_list_screenshots_path,
                                "pre_detail_screenshots_path": pre_detail_screenshots_path,
                                "pro_list_screenshots_path": pro_list_screenshots_path,
                                "pro_detail_screenshots_path": pro_detail_screenshots_path,
                                "list_diff_image_path": list_diff_image_path,
                                "detail_diff_image_path": detail_diff_image_path,

                                })
    return list_page_datas


def get_bd_urls():
    cate_name = 'bd'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, BD_PAGES, cate_name)


def get_mob_urls():
    cate_name = 'mob'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, MOB_PAGES, cate_name)


def get_jbd_urls():
    cate_name = 'jbd'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, JBD_PAGES, cate_name)


def get_sod_urls():
    cate_name = 'sod'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, SOD_PAGES, cate_name)


def get_acc_urls():
    cate_name = 'acc'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, ACC_PAGES, cate_name)


def get_sample_urls():
    cate_name = 'sample'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, SAMPLE_PAGES, cate_name)


def get_swatch_urls():
    cate_name = 'swatch'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, SWATCH_PAGES, cate_name)


def get_rts_urls():
    cate_name = 'rts'
    return handle_page_datas(PRO_BASE_URL, PRE_BASE_URL, RTS_PAGES, cate_name)


if __name__ == '__main__':
    li = get_bd_urls()
    for i in li:
        print(i)

