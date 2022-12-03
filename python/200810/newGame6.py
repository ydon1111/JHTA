#newGame1.py

import pygame 
import math
import random


#초기화
pygame.init()


def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))



screen_width= 600
screen_height =900

screen = pygame.display.set_mode((screen_width,screen_height))

isRunning = True

pygame.display.set_caption("우주 전쟁")


#배경 이미지 객체
bg1 = pygame.image.load("e:/dev/python_workspace/img/img/space.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/img/space.jpg")
#이미지 크기를 화면의 크기로 변환 
bg1 = pygame.transform.scale(bg1,(600,900))
bg2 = pygame.transform.scale(bg2,(600,900))

#배경 움직임
bg1Y = 0
bg2Y = -900
#비행기 연료
cnt = 0

#시계변수
clock = pygame.time.Clock()

#아군 비행기 객체

player1 = pygame.image.load("e:/dev/python_workspace/img/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/img/player4.png")

player1 = pygame.transform.scale(player1,(50,50))
player2 = pygame.transform.scale(player2,(50,50))
player3 = pygame.transform.scale(player3,(50,50))
player4 = pygame.transform.scale(player4,(50,50))


#적 비행기 객체 

gunship0 = pygame.image.load("e:/dev/python_workspace/img/img/gunship0.png")
gunship1 = pygame.image.load("e:/dev/python_workspace/img/img/gunship1.png")
gunship2 = pygame.image.load("e:/dev/python_workspace/img/img/gunship2.png")
gunship3 = pygame.image.load("e:/dev/python_workspace/img/img/gunship3.png")

gunship0 = pygame.transform.scale(gunship0,(50,50))
gunship1 = pygame.transform.scale(gunship1,(50,50))
gunship2 = pygame.transform.scale(gunship2,(50,50))
gunship3 = pygame.transform.scale(gunship3,(50,50))


#미사일 그리기 
missile = pygame.image.load("e:/dev/python_workspace/img/img/missile1.png")
#미사일 좌표
mX = -250
mY = -300

mList = []

class Missile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __del__(self):
        pass
        # print("소멸자 미사일 제거됨")


# 아군 우주선 좌표

px = 250
py = 800

# 적군 우주선 좌표

gx = 250
gy = 200

while isRunning:
    cnt +=1
    bg1Y +=2
    bg2Y +=2 
    gy +=1 
    


    if bg1Y > 900:
        bg1Y = -900
        bg2Y = 0 
    if bg2Y > 900:
        bg2Y = -900
        bg1Y = 0
    fps = clock.tick(60) #화면에 초당 프레임수 30
    
    #현재 프레임 수 확인
    # print("fps :" ,str(clock.get_fps()))
    
    for event in pygame.event.get():
            if event.type== pygame.QUIT:
                isRunning = False 

            if event.type == pygame.MOUSEBUTTONDOWN:
                mX,mY = pygame.mouse.get_pos()
                mList.append(Missile(mX,mY))

    #배경그리기 
    screen.blit(bg1,(0,bg1Y))
    screen.blit(bg2,(0,bg2Y))

    #마우스 좌표구하기
    # print(pygame.mouse.get_pos())
    px, py = pygame.mouse.get_pos()


    #아군 비행기
    if cnt%4 == 0:
        screen.blit(player1,(px-25,py-25))
    elif cnt%4 ==1:
        screen.blit(player2,(px-25,py-25))
    elif cnt%4 ==2:
        screen.blit(player3,(px-25,py-25))
    elif cnt%4 ==3:
        screen.blit(player4,(px-25,py-25))
    

    #적군 비행기
    if cnt%4 == 0:
        screen.blit(gunship0,(gx-25,gy-25))
    elif cnt%4 == 1:
        screen.blit(gunship1,(gx-25,gy-25))
    elif cnt%4 == 2:
        screen.blit(gunship2,(gx-25,gy-25))
    elif cnt%4 == 3:
        screen.blit(gunship3,(gx-25,gy-25))
    
    
    # screen.blit(missile,(mX,mY))


    #미사일 그리기 
    for m in mList:
        screen.blit(missile,(m.x,m.y))
        m.y -= 5
        if m.y <= -50:
            mList.remove(m)
            del(m)

        

    
    
    
    



    pygame.display.update()






pygame.quit()