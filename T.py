import requests
from base_path import screenshots_path
import os
from common.handle_red_conf_file import cf

PRO_BASE_URL = cf.get_str('URL', 'PRO_BASE_URL')
PRE_BASE_URL = cf.get_str('URL', 'PRE_BASE_URL')


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


def get_acc_category_items():
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


def generate_page_datas(pro_url, pre_url, category_items, page_name, quick_shop):
    """

    :param pro_url:
    :param pre_url:
    :param page_items:
    :param cate_name:
    :return:
    """
    page_datas = []
    base_path = os.path.join(screenshots_path, page_name)

    for page_items in category_items:
        cate_name = page_items['cat_name']
        page_url = page_items['url']

        pre_list_screenshots_path = os.path.join(screenshots_path, page_name, cate_name + "_list_pre.png")
        pre_detail_screenshots_path = os.path.join(screenshots_path, page_name, cate_name + "_detail_pre.png")
        pro_list_screenshots_path = os.path.join(screenshots_path, page_name, cate_name + "_list_pro.png")
        pro_detail_screenshots_path = os.path.join(screenshots_path, page_name, cate_name + "_detail_pro.png")
        list_diff_image_path = os.path.join(screenshots_path, page_name, cate_name + "_list_diff.png")
        detail_diff_image_path = os.path.join(screenshots_path, page_name, cate_name + "_detail_diff.png")

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


def get_acc_page_data():
    page_name = 'acc'
    quick_shop = True
    acc_datas = generate_page_datas(PRO_BASE_URL, PRE_BASE_URL, get_acc_category_items(), page_name, quick_shop)
    return acc_datas


if __name__ == '__main__':
    print(get_acc_page_data())
