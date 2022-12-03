from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#selenium
#웹브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 프로젝트

# webdriver

#브라우저 버전확인 
# chrome://version/
# 84.0.4147.125
# https://chromedriver.chromium.org/downloads

browser = webdriver.Chrome("e:/dev/chromedriver.exe")  #크롬드라이버 설치경로로 명시해야함 현재 python_workspace 에 있어서 별도로 안적음 
browser.get("http://www.naver.com")
element = browser.find_element_by_id("query")
time.sleep(3)
element.click()
element.send_keys("택배 없는 날 ")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.get("http://google.com")

element = browser.find_element_by_name("q")
#엘리먼트를 클릭
element.click()
#검색키워드를 입력 
element.send_keys("광복절")
element.send_keys(Keys.ENTER)
time.sleep(3)
element.click()
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys("휴일")
element.send_keys(Keys.ENTER)
