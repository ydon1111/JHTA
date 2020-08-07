import pygame
import time 


pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))

#배경그리기
bg = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
#토끼 그리기 
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit2.png')
#토끼 사이즈 조절
rabbit1 = pygame.transform.scale(rabbit1,(100,100))
rabbit2 = pygame.transform.scale(rabbit2,(100,100))



isRunning = True #게임을 계속 진행할지 , 중지 할지를 결정하는 변수 
pygame.display.set_caption("토끼 사냥")

rx = 100
ry = 200

# count = 0 
cnt = 0 
while isRunning:
    cnt += 1 
    for event in pygame.event.get():  #이벤트 모으기 
        if event.type == pygame.QUIT:
            isRunning = False

        keys = pygame.key.get_pressed()
        # print(keys[pygame.K_LEFT])
    
    if keys[pygame.K_LEFT] == 1:  #왼족 화살표 버튼이 눌리면상태면
        if count == 5 :
            rx -= 5 
            count = 0 
        else:
            count += 1
    if keys[pygame.K_UP] == 1:
        if count == 5 :
            ry -= 5 
            count = 0 
        else:
            count += 1
    if keys[pygame.K_DOWN] ==1 :
        if count == 5 :
            ry += 5 
            count = 0 
        else:
            count += 1
    if keys[pygame.K_RIGHT] ==1:
        if count == 5 :
            rx += 5 
            count = 0   
        else:
            count += 1
        
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
    screen.blit(bg,(0,0))
    
    # time.sleep(0.1)
    if  cnt%2 == 0:
        screen.blit(rabbit1,(rx,ry))
    else: 
        screen.blit(rabbit2,(rx,ry))
    
    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()