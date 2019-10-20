import requests
import json

#url = "http://cuiqingcai.com"
# r = requests.get(url)
# print(type(r))
# print(r.status_code)
# print(r.encoding)
# print(r.content)
# print(r.text)
# print(r.cookies)

# payload = {'key1': 'value1', 'key2': 'value2'}
# # r = requests.get('http://httpbin.org/get', params=payload)
# # print(r.url)
# headers = {'content-type': 'application/json'}
# # r = requests.get('http://httpbin.org/get', params=payload, headers=headers)
# # print(r.url)
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# url = "http://httpbin.org/post"
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# print(r.text)

url = 'http://httpbin.org/post'
files = {'file': open('a.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)