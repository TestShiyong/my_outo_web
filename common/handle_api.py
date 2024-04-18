import requests


def find_content_goods_number(url, datas, country, language):
    new_header = {"Content-Type": "application/json",
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
        result = requests.post(url, json=datas, headers=new_header)
        goods_number = len(result.json()['data']['prodList'])
        return goods_number
    except Exception as e:
        print(f"HTTP请求错误: {e}")



if __name__ == '__main__':
    data = {"filters": {}, "view_mode": ["petite"], "originUrl": "/all/accessories?sort_by=popularity&page=1"}
    url = 'https://apix-p2.azazie.com/1.0/list/content?format=list&cat_name=accessories&dress_type=dress&page=1&limit=60&in_stock=&sort_by=popularity&gtopic=azazie&listColorVersion=A'

    print(find_content_goods_number(url, data, 'us', 'en'))
