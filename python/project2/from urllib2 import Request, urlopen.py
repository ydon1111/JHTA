import xmltodict
import requests
import pandas as pd

url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'iSQ7gwjVu4haAwa3pC4MWU47J2dBYRQueiynfEEVhkQe84qE4iAvL7Nu9VEiXVIYdxzbdtsTzXK2aKc8F%2FXkBA%3D%3D', quote_plus('goodId') : '335' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)    



url = http://openapi.seoul.go.kr:8088/sample/xml/SebcArtGalleryKor/1/5/
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '	675558684b6b796439347964784344', quote_plus('goodId') : '335' })

675558684b6b796439347964784344 









