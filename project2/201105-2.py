import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

from xml.etree import ElementTree
from urllib.request import urlopen
import io

key = '675558684b6b796439347964784344' ### 여기에 신청한 본인의 key를 넣어야 합니다!

startpage = '1'
endpage = '5'
url = 'http://openapi.seoul.go.kr:8088/'+key+'/xml/culturalSpaceInfo/'+startpage+'/'+endpage+'/'
print(url)

XML_DF = requests.get(url).content
root = ElementTree.XML(XML_DF)

for child in root[2:]:
    for c in child:
        if c.tag == 'ADDR' : print(c.tag,c.text)
        

