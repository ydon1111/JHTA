from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "https://www.moakt.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)
time.sleep(2)
elem = browser.find_element_by_class_name("mail_in")
elem.click()
elem.send_keys("momstouch23556")
time.sleep(2)


time.sleep(2)
elem = browser.find_element_by_class_name("mail_butt")
elem.click()
time.sleep(2)

browser.find_element_by_class_name("iconic_button").click()

time.sleep(2)

elem = browser.find_element_by_name("mail_to")
elem.send_keys("momstouch23556@moakt.cc")

elem = browser.find_element_by_name("mail_subject")
elem.send_keys("메일전송 테스트")

elem = browser.find_element_by_name("mail_text")
elem.send_keys("asdflkdfgjlskdfjgoierjglsfkjglkfdjsglkjcvlbkjlkjglksdfjglkrjelgkjsd;lfkjlkjelrkslkn;lkjhnkljskljhglj")



pyautogui.alert("사람인걸 인증해주세요")

elem = browser.find_element_by_class_name("button-blue.subtit-button")
elem.click()

# print(pyautogui.position())



# name="mail_to"
# name="mail_subject"
# name="mail_text"


# https://www.moakt.com/ 임시메일 사이트