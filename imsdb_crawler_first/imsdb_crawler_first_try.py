import requests
import lxml.html
import re
from requests.exceptions import HTTPError

etree = lxml.html.etree

URLS = []


def collectURL():
    home_page = 'https://www.imsdb.com/all%20scripts/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    res = requests.get(home_page, headers)
    if res:
        html = etree.HTML(res.text)
        sub_url_count = html.xpath('count(/html/body[@id="mainbody"]/table[2]/tr/td[3]/p)')
        sub_url_count = int(sub_url_count)
        print(sub_url_count)
        base_url = '/html/body[@id="mainbody"]/table[2]/tr/td[3]/p[x]/a'
        for num in range(1, sub_url_count+1):
            base_path = base_url.replace(base_url[len(base_url) - 4], str(num))
            url = html.xpath(f'{base_path}/@href')
            url = f'https://www.imsdb.com{url[0]}'
            URLS.append(url)
        print(URLS)


def accessSubPage():
    '''
    Access to each sun page and collect message
    :param url:
    :return:
    '''


def collectScriptDetails():
    url = 'https://www.imsdb.com/Movie Scripts/10 Things I Hate About You Script.html'
    res = requests.get(url)
    if res:
        html = etree.HTML(res.text)
        # get title
        title = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[1]/td/h1')
        # get IMSDb options
        texts = html.xpath(
            '/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[2]/text()')
        # print(IMSDb_options)
        t = []
        for i in texts:
            if len(i.strip()) > 0:
                i = "".join(i.strip())
                t.append(i)
        options = t[0]

        # get IMSDb rating
        rating = float((t[1].replace("(", "").split())[0])
        average_user_rating = float((t[2].replace("(", "").split())[0])
        script_date = t[-1].replace(":", "").strip()
        print(title[0].text)
        print(t)
        print(options)
        print(rating)
        print(average_user_rating)
        print(script_date)

        # get writer
        writers = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[2]//a[contains(@href, "/writer")]/text()')
        print(writers)
        # get genres
        genres = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[2]//a[contains(@href, "/genre")]/text()')
        print(genres)

        # get image
        img = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[1]/img[@class="avimg"]/@src')
        print(img[0])

        b = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[2]//b/text()')
        print(b)

        c = html.xpath('/html/body[@id="mainbody"]/table[2]/tr/td[3]/table[@class="script-details"]/tr[2]/td[2]')
        print(c[0].xpath('string(.)').strip())
        d = c[0].xpath('string(.)').strip()
        e = d.split(u'\r\n')
        e = [item for item in e if len(item.split()) > 0]
        e = [item.replace(u'\t', '') for item in e]
        e = [item.replace(u'\xa0\xa0', ':') for item in e]
        e = [" ".join(item.split()) for item in e]
        print(e)
        for i in range(len(e)):
            if 'IMSDb opinion' in e[i]:
                IMSDB_opinion = (e[i].split(":"))[1]
                print(IMSDB_opinion)
            elif 'IMSDb rating'in e[i]:
                pattern = re.compile(r'\d+')
                IMSDB_rating = pattern.search((e[i].split(":"))[1])
                print(float(IMSDB_rating.group()))
            elif 'Average user rating' in e[i]:
                pattern = re.compile(r'(-?\d+)(\.\d+)?')
                average_user_rating = pattern.search((e[i].split(":"))[1])
                print(float(average_user_rating.group()))
            elif 'Script Date' in e[i]:
                script_date = (e[i].split(":"))[1]
                print(script_date.strip())
            elif 'Movie Release Date' in e[i]:
                movie_release_date = (e[i].split(":"))[1]
                print(movie_release_date)

# collectURL()
collectScriptDetails()
