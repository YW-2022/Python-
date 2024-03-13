import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type':'11',
        'interval_id':'10:0',
        'action':'',
        'start':'0',
        'limit':'20'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)

    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('Over!!!')










