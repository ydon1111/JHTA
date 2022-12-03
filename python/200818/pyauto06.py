from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "http://www.naver.com"

browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")

browser.get(url)

#화면 최대로 
browser.maximize_window()

elem =browser.find_element_by_id("query")
elem.click()
elem.send_keys("종로3가맛집")
elem.send_keys(Keys.ENTER)

time.sleep(2)

#아래로 스크롤
pyautogui.scroll(-1500)

for i in range(1,21):
    ulElem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")
    # print(ulElem)

    lists = ulElem.find_elements_by_css_selector(".list_item.type_restaurant")
    # print(lists)

    for store in lists:
        print(store.find_element_by_css_selector("div.tit > span > a > span").text)
    print("------------------------------------------")

    pyautogui.click(764,630)
    
    # time.sleep(3)

    ulElem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")
    # print(ulElem)
    lists = ulElem.find_elements_by_css_selector(".list_item.type_restaurant")
    # print(lists)

    for store in lists:
        print(store.find_element_by_css_selector("div.tit > span > a > span").text)
        print("--------------------------------")