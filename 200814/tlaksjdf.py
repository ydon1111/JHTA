from selenium import webdriver

browser = webdriver.Chrome()  
browser.get("http://www.naver.com")
element = browser.find_element_by_id("query")
element.click()
element.send_keys("택배 없는 날 ")