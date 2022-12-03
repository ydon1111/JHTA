import pygame
import time 


pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))

#배경그리기
bg = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit2.png')

isRunning = True #게임을 계속 진행할지 , 중지 할지를 결정하는 변수 
pygame.display.set_caption("토끼 사냥")

rx = 100
ry = 200


cnt = 0 
while isRunning:
    cnt += 1 
    for event in pygame.event.get():  #이벤트 모으기 
        if event.type == pygame.QUIT:
            isRunning = False
#게임이 진행되는 동안
    #배경그리기
    # print(cnt)
    screen.blit(bg,(0,0))
    
    time.sleep(0.1)
    if  cnt%2 == 0:
        screen.blit(rabbit1,(rx,ry))
    else: 
        screen.blit(rabbit2,(rx,ry))
    
    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()