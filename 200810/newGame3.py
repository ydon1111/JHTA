#newGame1.py

import pygame 

#초기화
pygame.init()


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

while isRunning:
    cnt +=1
    bg1Y +=2
    bg2Y +=2 

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
    #배경그리기 
    screen.blit(bg1,(0,bg1Y))
    screen.blit(bg2,(0,bg2Y))



    #아군 비행기
    if cnt%4 == 0:
        screen.blit(player1,(250,800))
    elif cnt%4 ==1:
        screen.blit(player2,(250,800))
    elif cnt%4 ==2:
        screen.blit(player3,(250,800))
    elif cnt%4 ==3:
        screen.blit(player4,(250,800))
    

    
    
    
    



    pygame.display.update()






pygame.quit()