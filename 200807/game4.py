import pygame
import time 


pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))

#배경그리기
bg1 = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
bg2 = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
#배경 사이즈 조절 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))


#토끼 그리기 
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit2.png')
#토끼 사이즈 조절
rabbit1 = pygame.transform.scale(rabbit1,(100,100))
rabbit2 = pygame.transform.scale(rabbit2,(100,100))
#시계변수

clock = pygame.time.Clock()


isRunning = True #게임을 계속 진행할지 , 중지 할지를 결정하는 변수 
pygame.display.set_caption("토끼 사냥")

#토끼 시작좌표 
rx = 100
ry = 200

#배경 좌표
bg1X = 0 
bg2X = 1200 

cnt = 0 
while isRunning:
    cnt += 1 
    bg1X -=2
    bg2X -=2 

    fps = clock.tick(120) #화면의 초당 프레임수 60

    #프레임이 얼마 인지 확인
    # print("fps :"+ str(clock.get_fps()))

    for event in pygame.event.get():  #이벤트 모으기 
        if event.type == pygame.QUIT:
            isRunning = False
    keys = pygame.key.get_pressed()
        # print(keys[pygame.K_LEFT])
    
    if keys[pygame.K_LEFT] == 1:  #왼족 화살표 버튼이 눌리면상태면 
        rx -= 5              
    if keys[pygame.K_UP] == 1:       
        ry -= 5        
    if keys[pygame.K_DOWN] ==1 :    
        ry += 5         
    if keys[pygame.K_RIGHT] ==1:
        rx += 5 
        
        
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         rx -= 5
        #     elif event.key == pygame.K_UP:
        #         ry -= 5 
        #     elif event.key == pygame.K_DOWN:
        #         rx += 5 
        #     elif event.key == pygame.K_RIGHT:
        #         ry += 5 
#게임이 진행되는 동안
    #배경그리기
    # print(cnt)
    
    screen.blit(bg1,(bg1X,0))
    screen.blit(bg2,(bg2X,0))

    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0 
    if bg2X <= -1200:
        bg2X = 1200
        bg1X = 0 



    # time.sleep(0.1)
    if  cnt%2 == 0:
        screen.blit(rabbit1,(rx,ry))
    else: 
        screen.blit(rabbit2,(rx,ry))
    
    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()