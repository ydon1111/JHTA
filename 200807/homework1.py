import pygame
import time 
import threading
import random
import math

pygame.init()


def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))


screen_width = 1200
screen_height =800

screen = pygame.display.set_mode((screen_width,screen_height))


bg1 = pygame.image.load('e:/dev/python_workspace/img/img/bg1.jpg')
bg2 = pygame.image.load('e:/dev/python_workspace/img/img/bg2.jpg')

bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))

run1 = pygame.image.load('e:/dev/python_workspace/img/img/run1.png')
run2 = pygame.image.load('e:/dev/python_workspace/img/img/run2.png')
run3 = pygame.image.load('e:/dev/python_workspace/img/img/run3.png')


gold = pygame.image.load('e:/dev/python_workspace/img/img/gold.png')
silver = pygame.image.load('e:/dev/python_workspace/img/img/silver.png')

# run1 = pygame.transform.scale(run1,(100,100))
# run2 = pygame.transform.scale(run2,(100,100))
# run3 = pygame.transform.scale(run3,(100,100))

clock = pygame.time.Clock()


isRunning = True
pygame.display.set_caption("고군분투")

rx = 100
ry = 490

bg1X = 0
bg2X = 1200

gX = 200
gY = 490

sX = 400
sY = 490


cnt = 0 
while isRunning:
    cnt += 1
    bg1X -=2
    bg2X -=2 
    gX -= 1
    sX -= 1

    fps = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    keys = pygame.key.get_pressed()


    if keys[pygame.K_RIGHT] == 1:
        rx += 5
        if rx >1100:
            rx = 1100
    if keys[pygame.K_LEFT] == 1:
        rx -= 5
        if rx <0:
            rx = 0

    if keys[pygame.K_SPACE] == 1:
        t = threading.Thread(target=self.jump)
        t.start()


    screen.blit(bg1,(bg1X,0))    
    screen.blit(bg2,(bg2X,0))

    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0
    if bg2X <= -1200:
        bg2X =1200
        bg1X = 0

    screen.blit(gold,(gX,gY))
    screen.blit(silver,(sX,sY))

    if gX <= -50:
        gX =  random.randint(100,1200)
        gY =  random.randint(300,500)
    if sX <= -50:
        sX =  random.randint(100,1200)
        sY =  random.randint(300,500)

    if cnt%3 ==0:
        screen.blit(run1,(rx,ry))
    elif cnt%3 ==1:
        screen.blit(run2,(rx,ry))   
    elif cnt%3 ==2:
        screen.blit(run3,(rx,ry))  


    dis = pythagoras(gX,gY,rx,ry)
    if dis <= 50:
        print("사라져라")

    pygame.display.update()

pygame.quit()