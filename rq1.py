import requests
import chardet

def get_page_content(url):
    # 发起请求
    response = requests.get(url=url)
    # 获取响应对象
    content = response.content

    # 使用 chardet 检测编码
    detected_encoding = chardet.detect(content)
    encoding = detected_encoding['encoding']

    # 解码内容
    page_text = content.decode(encoding, 'ignore')

    return page_text


if __name__ == "__main__":
    # 指定url
    url = 'https://www.bilibili.com/'
    # 获取页面内容
    page_text = get_page_content(url)

    # 持久存储
    with open('./bilibili.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('END!!!')
