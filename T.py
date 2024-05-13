import requests
from base_path import screenshots_path
import os
from common.handle_red_conf_file import cf

PRO_BASE_URL = cf.get_str('URL', 'PRO_BASE_URL')
PRE_BASE_URL = cf.get_str('URL', 'PRE_BASE_URL')


def get_list_content_goods_number(cat_name, origin_url, country='us', language='en'):
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


def get_acc_page_goods_number():
    cat_names = ['accessories', 'groomsmen-accessories', 'shoes', 'bags', 'jewelry', 'headpieces', 'shapewear', 'wraps',
                 'wedding-veils', 'sashes', 'robes', 'gifts', 'separates', 'garment-bags']

    origin_urls = ["/all/accessories", "/all/groomsmen-accessories", "/all/shoes", "/all/bags", "/all/jewelry",
                   "/all/headpieces", "/all/shapewear", "/all/wraps", "/all/wedding-veils", "/all/sashes", "/all/robes",
                   "/all/gifts", "/all/separates", "/all/garment-bags"]

    # 存储结果的字典
    goods_numbers = {}

    # 遍历两个列表
    for cat_name, origin_url in zip(cat_names, origin_urls):
        goods_number = get_list_content_goods_number(cat_name, origin_url)
        goods_numbers[cat_name] = goods_number
    print(goods_numbers)
    return goods_numbers


def get_acc_url_datas():
    # goods_numbers = get_acc_page_goods_number()
    goods_numbers = {'accessories': 60, 'groomsmen-accessories': 59, 'shoes': 60, 'bags': 60, 'jewelry': 60,
                     'headpieces': 59, 'shapewear': 58, 'wraps': 60, 'wedding-veils': 60, 'sashes': 13, 'robes': 0,
                     'gifts': 28, 'separates': 24, 'garment-bags': 2}

    url_items = [
        # {'cat_name': 'accessories', 'url': '/all/accessories', 'goods_number': goods_numbers['accessories']},
        # {'cat_name': 'groomsmen-accessories', 'url': '/all/groomsmen-accessories',
        #  'goods_number': goods_numbers['groomsmen-accessories']},
        # {'cat_name': 'shoes', 'url': '/all/shoes', 'goods_number': goods_numbers['shoes']},
        # {'cat_name': 'bags', 'url': '/all/bags', 'goods_number': goods_numbers['bags']},
        # {'cat_name': 'jewelry', 'url': '/all/jewelry', 'goods_number': goods_numbers['jewelry']},
        # {'cat_name': 'headpieces', 'url': '/all/headpieces', 'goods_number': goods_numbers['headpieces']},
        # {'cat_name': 'shapewear', 'url': '/all/shapewear', 'goods_number': goods_numbers['shapewear']},
        # {'cat_name': 'wraps', 'url': '/all/wraps', 'goods_number': goods_numbers['wraps']},
        # {'cat_name': 'wedding-veils', 'url': '/all/wedding-veils', 'goods_number': goods_numbers['wedding-veils']},
        # {'cat_name': 'sashes', 'url': '/all/sashes', 'goods_number': goods_numbers['sashes']},
        {'cat_name': 'robes', 'url': '/all/robes', 'goods_number': goods_numbers['robes']},
        {'cat_name': 'gifts', 'url': '/all/gifts', 'goods_number': goods_numbers['gifts']},
        # {'cat_name': 'separates', 'url': '/all/separates', 'goods_number': goods_numbers['separates']},
        # {'cat_name': 'garment-bags', 'url': '/all/garment-bags', 'goods_number': goods_numbers['garment-bags']},
    ]

    return url_items


def handle_acc_datas(pro_url, pre_url, category_items, cate_name, quick_shop):
    """

    :param pro_url:
    :param pre_url:
    :param page_items:
    :param cate_name:
    :return:
    """
    page_datas = []
    for page_items in category_items:
        base_path = os.path.join(screenshots_path, cate_name)
        pre_list_screenshots_path = os.path.join(screenshots_path, cate_name, page_items['cat_name'] + "_list_pre.png")
        pre_detail_screenshots_path = os.path.join(screenshots_path, cate_name,
                                                   page_items['cat_name'] + "_detail_pre.png")
        pro_list_screenshots_path = os.path.join(screenshots_path, cate_name, page_items['cat_name'] + "_list_pro.png")
        pro_detail_screenshots_path = os.path.join(screenshots_path, cate_name,
                                                   page_items['cat_name'] + "_detail_pro.png")
        list_diff_image_path = os.path.join(screenshots_path, cate_name, page_items['cat_name'] + "_list_diff.png")
        detail_diff_image_path = os.path.join(screenshots_path, cate_name, page_items['cat_name'] + "_detail_diff.png")

        page_datas.append(
            {'pro_url': pro_url + page_items['url'], 'pre_url': pre_url + page_items['url'], 'base_path': base_path,
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


def get_acc_urls():
    cate_name = 'acc'
    quick_shop = True
    acc_datas = handle_acc_datas(PRO_BASE_URL, PRE_BASE_URL, get_acc_url_datas(), cate_name, quick_shop)
    return acc_datas


if __name__ == '__main__':
    print(get_acc_urls())
