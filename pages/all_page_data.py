from common.handle_red_conf_file import cf
from base_path import screenshots_path
import os
import requests

PRO_BASE_URL = cf.get_str('URL', 'PRO_BASE_URL')
PRE_BASE_URL = cf.get_str('URL', 'PRE_BASE_URL')

custom_p_number = 1
# {'cat_name':
#  ,'url'
custom_pre_url = f'https://p{custom_p_number}.azazie.com'
BD_PAGE_URLS = [{'cat_name': 'list_page_bd_url', 'url': '/all/bridesmaid-dresses'},
                {'cat_name': 'list_page_bd_plus_size_url', 'url': '/all/plus-size-bridesmaid-dresses'},
                {'cat_name': 'list_page_maternity_url', 'url': '/all/maternity-bridesmaid-dresses'},
                {'cat_name': 'list_page_modest_url', 'url': '/all/modest-bridesmaid-dresses'}]

# MOB
MOB_PAGE_URLS = [{'cat_name': 'list_page_mother_url', 'url': '/all/mother-of-the-bride-dresses'},
                 {'cat_name': 'list_page_plus_sie_mob_url', 'url': '/all/plus-size-mother-of-the-bride-dresses'}]

JBD_PAGE_URLS = [{'cat_name': 'list_page_all_jbd_url', 'url': '/all/all-junior'},
                 {'cat_name': 'list_page_junior_url', 'url': '/all/junior-bridesmaid-dresses'},
                 {'cat_name': 'list_page_flower_url', 'url': '/all/flower-girl-dresses'}, ]

SOD_PAGE_URLS = [{'cat_name': 'list_page_sod_url', 'url': '/all/atelier-dresses'}]

SAMPLE_PAGE_URLS = [
    # 'list_page_all_sample_url': '/all/sample-dresses?current_in_stock=yes'},
    {'cat_name': 'list_page_wd_sample_url', 'url': '/all/sample-brides?current_in_stock=yes'},
    {'cat_name': 'list_page_bd_sample_url', 'url': '/all/sample-bridesmaids?sort_by=popularity&current_in_stock=yes'},
    {'cat_name': 'list_page_maternity_sample_url', 'url': 'sort_by=popularity&current_in_stock=yes'},
    {'cat_name': 'list_page_modest_sample_url', 'url': '/all/sample-modest?sort_by=popularity&current_in_stock=yes'},
    {'cat_name': 'list_page_mother_sample_url',
     'url': '/all/sample-mother-of-the-bride?sort_by=popularity&current_in_stock=yes'},
    {'cat_name': 'list_page_junior_sample_url',
     'url': '/all/sample-junior-bridesmaid-dresses?sort_by=popularity&current_in_stock=yes'}]

SWATCH_PAGE_URLS = [{'cat_name': 'list_page_swatch_fabric_url', 'url': '/swatches-fabric'},
                    {'cat_name': 'list_page_swatches_url', 'url': '/all/swatches'},
                    {'cat_name': 'list_page_fabrics_url', 'url': '/all/fabrics'}]

RTS_PAGE_URLS = [
    {'cat_name': "list_page_all_rts_url", 'url': "/all/final-sale"},
    {'cat_name': "list_page_bd_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-bridesmaids?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_mob_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-mother-of-the-brides?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_wd_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-brides?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_sod_rts_url",
     'url': "/all/final-sale/with/category/special-offer-special-occasion-dresses?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_flower_rts_url",
     'url': "/all/final-sale/with/category/special-offer-flower-girl-dresses?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_junior_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-junior-bridesmaid-dresses?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_groomsmen_rts_url",
     'url': "/all/final-sale/with/category/special-offer-groomsmen-accessories?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_maternity_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-maternity?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_modest_rts_url",
     'url': "/all/final-sale/with/category/ready-to-ship-modest?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_shoes_rts_url",
     'url': "/all/final-sale/with/category/special-offer-shoes?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_bags_rts_url",
     'url': "/all/final-sale/with/category/special-offer-bags?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_jewelry_rts_url",
     'url': "/all/final-sale/with/category/special-offer-jewelry?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_headpieces_rts_url",
     'url': "/all/final-sale/with/category/special-offer-headpieces?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_shapewear_rts_url",
     'url': "/all/final-sale/with/category/special-offer-shapewear?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_wrap_rts_url",
     'url': "/all/final-sale/with/category/special-offer-wraps?sort_by=popularity&current_in_stock=yes"},
    {'cat_name': "list_page_veils_rts_url",
     'url': "/all/final-sale/with/category/special-offer-wedding-veils?sort_by=popularity&current_in_stock=yes"}]


def generate_category_datas(pro_url, pre_url, category_items, page_name, quick_shop):
    """

    :param pro_url:
    :param pre_url:
    :param page_items:
    :param page_name:
    :return:
    """
    page_datas = []
    base_path = os.path.join(screenshots_path, page_name)

    for page_items in category_items:
        cat_name = page_items['cat_name']
        page_url = page_items['url']

        pre_list_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_list_pre.png")
        pre_detail_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_detail_pre.png")
        pro_list_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_list_pro.png")
        pro_detail_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_detail_pro.png")
        list_diff_image_path = os.path.join(screenshots_path, page_name, 'diff', cat_name + "_list_diff.png")
        detail_diff_image_path = os.path.join(screenshots_path, page_name, 'diff', cat_name + "_detail_diff.png")

        page_datas.append(
            {'pro_url': pro_url + page_url, 'pre_url': pre_url + page_url, 'base_path': base_path,
             "pre_list_screenshots_path": pre_list_screenshots_path,
             "pre_detail_screenshots_path": pre_detail_screenshots_path,
             "pro_list_screenshots_path": pro_list_screenshots_path,
             "pro_detail_screenshots_path": pro_detail_screenshots_path,
             "list_diff_image_path": list_diff_image_path,
             "detail_diff_image_path": detail_diff_image_path,
             "quick_shop": quick_shop
             })
    return page_datas


def get_list_content_goods_number(cat_name, origin_url, country='us', language='en'):
    """
    获取列表页商品数量
    :param cat_name:
    :param origin_url:
    :param country:
    :param language:
    :return:
    """
    url = f'https://www.azazie.com/prod/1.0/list/content?format=list&cat_name={cat_name}&dress_type=dress&page=1&limit=60&in_stock=&sort_by=popularity&is_outlet=0&version=b&activityVerison=a&galleryVersion=B&sodGalleryVersion=B&topic=azazie&listColorVersion=A'
    data = {"filters": {}, "view_mode": ["petite"], "originUrl": f"{origin_url}?sort_by=popularity"}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-app": "pc",
        "x-token": "",
        "x-project": "azazie",
        "x-countryCode": country,
        "authorization": "Basic bGViYmF5OnBhc3N3MHJk",
        "x-languageCode": language,
        "cache-action": "flush"
    }
    try:
        result = requests.post(url, json=data, headers=headers).json()['data']
        empty = 'empty'
        if empty in result:
            return 0
        else:
            goods_number = len(result['prodList'])
            return goods_number
    except Exception as e:
        print(f"HTTP请求错误: {e}, url={url}")
        return 0


def get_acc_url_and_cat_name():
    acc_page_data = [
        {'cat_name': 'accessories', 'url': '/all/accessories'},
        {'cat_name': 'groomsmen-accessories', 'url': '/all/groomsmen-accessories'},
        {'cat_name': 'shoes', 'url': '/all/shoes'},
        {'cat_name': 'bags', 'url': '/all/bags'},
        {'cat_name': 'jewelry', 'url': '/all/jewelry'},
        {'cat_name': 'headpieces', 'url': '/all/headpieces'},
        {'cat_name': 'shapewear', 'url': '/all/shapewear'},
        {'cat_name': 'wraps', 'url': '/all/wraps'},
        {'cat_name': 'wedding-veils', 'url': '/all/wedding-veils'},
        {'cat_name': 'sashes', 'url': '/all/sashes'},
        {'cat_name': 'robes', 'url': '/all/robes'},
        {'cat_name': 'gifts', 'url': '/all/gifts'},
        {'cat_name': 'separates', 'url': '/all/separates'},
        {'cat_name': 'garment-bags', 'url': '/all/garment-bags'}
    ]
    for item in acc_page_data:
        item['goods_number'] = get_list_content_goods_number(item['cat_name'], item['url'])

    return acc_page_data


def generate_acc_datas(pro_url, pre_url, category_items, page_name, quick_shop):
    """

    :param pro_url:
    :param pre_url:
    :param page_items:
    :param cat_name:
    :return:
    """
    page_datas = []
    base_path = os.path.join(screenshots_path, page_name)

    for page_items in category_items:
        cat_name = page_items['cat_name']
        page_url = page_items['url']

        pre_list_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_list_pre.png")
        pre_detail_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_detail_pre.png")
        pro_list_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_list_pro.png")
        pro_detail_screenshots_path = os.path.join(screenshots_path, page_name, cat_name + "_detail_pro.png")
        list_diff_image_path = os.path.join(screenshots_path, page_name, cat_name + "_list_diff.png")
        detail_diff_image_path = os.path.join(screenshots_path, page_name, cat_name + "_detail_diff.png")

        page_datas.append(
            {'pro_url': pro_url + page_url, 'pre_url': pre_url + page_url, 'base_path': base_path,
             "pre_list_screenshots_path": pre_list_screenshots_path,
             "pre_detail_screenshots_path": pre_detail_screenshots_path,
             "pro_list_screenshots_path": pro_list_screenshots_path,
             "pro_detail_screenshots_path": pro_detail_screenshots_path,
             "list_diff_image_path": list_diff_image_path,
             "detail_diff_image_path": detail_diff_image_path,
             "quick_shop": quick_shop,
             "goods_number": page_items['goods_number']
             })
    return page_datas


def get_bd_datas():
    page_name = 'bd'
    quick_shop = False
    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, BD_PAGE_URLS, page_name, quick_shop)


def get_mob_datas():
    page_name = 'mob'
    quick_shop = False

    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, MOB_PAGE_URLS, page_name, quick_shop)


def get_jbd_datas():
    page_name = 'jbd'
    quick_shop = False
    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, JBD_PAGE_URLS, page_name, quick_shop)


def get_sod_datas():
    page_name = 'sod'
    quick_shop = False

    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, SOD_PAGE_URLS, page_name, quick_shop)


def get_acc_datas():
    page_name = 'acc'
    quick_shop = True
    return generate_acc_datas(PRO_BASE_URL, PRE_BASE_URL, get_acc_url_and_cat_name(), page_name, quick_shop)


def get_sample_datas():
    page_name = 'sample'
    quick_shop = False
    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, SAMPLE_PAGE_URLS, page_name, quick_shop)


def get_swatch_datas():
    page_name = 'swatch'
    quick_shop = True

    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, SWATCH_PAGE_URLS, page_name, quick_shop)


def get_rts_datas():
    page_name = 'rts'
    quick_shop = False
    return generate_category_datas(PRO_BASE_URL, PRE_BASE_URL, RTS_PAGE_URLS, page_name, quick_shop)


if __name__ == '__main__':
    li = get_bd_datas()
    for i in li:
        print(i)
    # li2 = get_bd_urls()
    # for j in li2:
    #     print(j)
