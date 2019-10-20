import lxml.html
etree = lxml.html.etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html, pretty_print=True)
# print(result.decode('utf-8'))

html = etree.parse('hello.html')
print(type(html))
# 获取所有<li>标签
result = html.xpath('//li')
# 获取<li>标签的所有class
result = html.xpath('//li/@class')
# 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result = html.xpath('//li/a[@href="link1.html"]')
# 获取 <li> 标签下的所有 <span> 标签
result = html.xpath('//li//span')
# 获取 <li> 标签下的所有 class，不包括 <li>
result = html.xpath('//li/a//@class')
# 获取最后一个 <li> 的 <a> 的 href
result = html.xpath('//li[last()]/a/@href')
# 获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
# 获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print(result)
print(len(result))
print(result[0].tag)
