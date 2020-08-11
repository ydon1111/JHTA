import pygame
import random


pygame.init()

screen_width =1200
screen_height = 800

#배경 이미지 객체
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")
bg = pygame.transform.scale(bg,(1200,800))


ball = pygame.image.load("e:/dev/python_workspace/img/img/gold.png")
ball = pygame.transform.scale(ball,(100,100))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("핑퐁")

bx = 600
by = 400
inc_x =random.randint(-10,10)
inc_y =random.randint(-10,10)import pygame
import random


pygame.init()

screen_width =1200
screen_height = 800

#배경 이미지 객체
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")
bg = pygame.transform.scale(bg,(1200,800))


ball = pygame.image.load("e:/dev/python_workspace/img/img/gold.png")
ball = pygame.transform.scale(ball,(100,100))

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("핑퐁")

bx = 600
by = 400
inc_x =random.randint(-10,10)
inc_y =random.randint(-10,10)

clock = pygame.time.Clock()


def changeDirection(x,y,ix,iy):
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정
    if y <=0 or y >=730:
        iy = -iy 
    if x <=0 or x >=1130:
        ix = -ix
    # elif x <= 3: 
    #     ix = -ix
    # elif x <= 1100:
    #     ix = -ix
    
    return ix,iy




isRunning = True 
while isRunning:
    bx -= inc_x 
    by -= inc_y

    fps = clock.tick(60)  #화면의 프레임수 

    inc_x ,inc_y = changeDirection(bx,by,inc_x,inc_y)
   
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 

    screen.blit(bg,(0,0))

    screen.blit(ball,(bx,by))


    pygame.display.update()

pygame.display.update()

pygame.quit()

clock = pygame.time.Clock()


def changeDirection(x,y,ix,iy):
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정
    if y <=0 or y >=730:
        iy = -iy 
    if x <=0 or x >=1130:
        ix = -ix
    # elif x <= 3: 
    #     ix = -ix
    # elif x <= 1100:
    #     ix = -ix
    
    return ix,iy




isRunning = True 
while isRunning:
    bx -= inc_x 
    by -= inc_y

    fps = clock.tick(60)  #화면의 프레임수 

    inc_x ,inc_y = changeDirection(bx,by,inc_x,inc_y)
   
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 

    screen.blit(bg,(0,0))

    screen.blit(ball,(bx,by))


    pygame.display.update()

pygame.display.update()

pygame.quit()