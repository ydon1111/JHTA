import requests

url ="http://www.naver.com"

res = requests.get(url)
res.raise_for_status()
# print(res)
# print(res.status_code)
# print(res.text)

