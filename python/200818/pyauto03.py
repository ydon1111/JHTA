import pyautogui
import time 


pyautogui.moveTo(400,400,2) #x,y,이동시간

#moveToRel() 상대거리
#moveTo() 절대거리

pyautogui.moveRel(100,100,3)
pyautogui.click(clicks=2,interval=2) #클릭횟수 , 간격

pyautogui.doubleClick()

time.speed(1)
pyautogui.typewrite('hello')