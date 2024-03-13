import requests

# UA: User-Agent 请求载体的身份标识
# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
# 那么意味着当前请求为正常浏览器的正常请求；但是如果检测到不是基于某一款浏览器的，则标识该请求为不正常请求（爬虫）。
# UA伪装：反反爬策略，让爬虫对应的请求载体身份标识伪装成某一款具体的浏览器

if __name__ == "__main__":
    # UA伪装：
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    # 处理url所携带的参数：封装到字典中
    kw = input('enter a word: ')
    param = {
        'query':kw
    }
    # 对指定url发起的请求是携带的参数的，并且请求过程中已经处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    # 获取相应数据
    page_text = response.text

    # 将相应数据写入html中
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')


