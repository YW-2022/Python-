import json

import requests

if __name__ == "__main__":
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装 - 在requests请求之前进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    # 3.post请求参数处理
    word = input('Enter a word: ')
    data = {
        'kw':word
    }
    # 4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    # 5.获取相应数据: json()方法返回的是obj(这个需要具体查看它的返回类型做对应，也有可能它本身返回的是list）
    dic_obj = response.json()
    print(dic_obj)

    # 6.进行持久存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!')






