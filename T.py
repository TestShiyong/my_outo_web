import requests


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
    goods_numbers = get_acc_page_goods_number()
    url_items = [{'list_page_all_acc_url': '/all/accessories', 'goods_number': goods_numbers['accessories']},
                 {'list_page_groomsmen_rul': '/all/groomsmen-accessories',
                  'goods_number': goods_numbers['groomsmen-accessories']},
                 {'list_page_shoes_url': '/all/shoes', 'goods_number': goods_numbers['shoes']},
                 {'list_page_bags_url': '/all/bags', 'goods_number': goods_numbers['bags']},
                 {'list_page_jewelry_url': '/all/jewelry', 'goods_number': goods_numbers['jewelry']},
                 {'list_page_shapewear': '/all/shapewear', 'goods_number': goods_numbers['headpieces']},
                 {'list_page_wraps': '/all/wraps', 'goods_number': goods_numbers['shapewear']},
                 {'list_page_headpieces': '/all/headpieces', 'goods_number': goods_numbers['wraps']},

                 {'list_page_wedding_veils': '/all/wedding-veils', 'goods_number': goods_numbers['wedding-veils']},
                 {'list_page_sashes': '/all/sashes', 'goods_number': goods_numbers['sashes']},
                 {'list_page_robes': '/all/robes', 'goods_number': goods_numbers['robes']},
                 {'list_page_gifts': '/all/gifts', 'goods_number': goods_numbers['gifts']},
                 {'list_page_separates': '/all/separates', 'goods_number': goods_numbers['separates']},
                 {'list_page_garment_bags': '/all/garment-bags', 'goods_number': goods_numbers['garment-bags']}
                 ]

    return url_items


if __name__ == '__main__':
    print(get_acc_url_datas())
