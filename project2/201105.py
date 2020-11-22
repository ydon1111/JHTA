import xmltodict
import requests
import pandas as pd

url = 'http://openapi.seoul.go.kr:8088/sample/xml/SebcArtGalleryKor/1/5/'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '675558684b6b796439347964784344 '})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)    
   
   




