import lxml.html
import requests

etree = lxml.html.etree


# Sub page url
URL = []


def generate_sub_urls(main_url: str):
    """Generate all sub urls.
    Args:
        main_url : (str) the URL for home page.
    Return:
        URL : (list) the list of sub page URL
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    response = requests.get(main_url, headers)
    if response:
        html = etree.HTML(response.text)




