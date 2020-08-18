from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

url = "https://www.naver.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)
time.sleep(2)
elem = browser.find_element_by_class_name("link_login")
elem.click()


elem = browser.find_element_by_id("id")
elem.send_keys("kyd5022")


elem = browser.find_element_by_id("pw")
elem.send_keys("aaaaaaaaaaaaa")
time.sleep(2)


elem = browser.find_element_by_id("log.login")
elem.click()


pyautogui.alert("로그인 완료후 버튼 클릭")
browser.maximize_window()

pyautogui.click(1339 , 516)

pyautogui.click(1483,554)

time.sleep(2)
# pip install pyperclip
#받는사람
pyautogui.click(442,347)
pyautogui.write("kyd5022@naver.com")



pyautogui.click(800, 419)
pyperclip.copy("메일 테스트")
pyautogui.hotkey("ctrl","v")


pyautogui.click(357, 600)
pyperclip.copy("가낟라ㅏ마ㅏ마바사아자나남아차")
pyautogui.hotkey("ctrl","v")


time.sleep(2)

pyautogui.click(294, 293)


# browser.find_element_by_css_selector(".tab_MY_TAP_MAIL").click()
# browser.find_element_by_css_selector(".func").click()






# https://www.moakt.com/ 임시메일 사이트

