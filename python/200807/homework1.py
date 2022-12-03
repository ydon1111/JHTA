import pygame
import time 
import threading
import random
import math
import threading

pygame.init()



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

gold = pygame.transform.scale(gold,(50,50))
silver = pygame.transform.scale(silver,(50,50))

run1 = pygame.transform.scale(run1,(100,100))
run2 = pygame.transform.scale(run2,(100,100))
run3 = pygame.transform.scale(run3,(100,100))

clock = pygame.time.Clock()


isRunning = True
pygame.display.set_caption("고군분투")

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS",30)

rx = 150
ry = 540

bg1X = 0
bg2X = 1200

gX = 200
gY = 490

sX = 400
sY = 490


goldList = []
silverList = []
def gcoin():
    c = MakeCoin(1300,random.randint(300,490))
    goldList.append(c)
def scoin():
    c = MakeCoin(1300,random.randint(300,490))
    silverList.append(c)

def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

def jump():
    global ry,rx
    for i in range(3):
        time.sleep(0.07)
        ry -= 3
        rx += 1
    for r in range(3):
        time.sleep(0.07)
        ry += 3
        rx += 1

class MakeCoin:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def __del__(self):
        pass

def collision(x1,y1,x2,y2):
    dis = pythagoras(x1,y1,x2,y2)
    result = 0   
    if dis <40:
        result=1
    return result


score = 0
cnt = 0 
while isRunning:
    cnt += 1
    bg1X -=2
    bg2X -=2 
    # gX -= 1
    # sX -= 1
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
        t= threading.Thread(target=jump)
        t.start()


    screen.blit(bg1,(bg1X,0))    
    screen.blit(bg2,(bg2X,0))
    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0
    if bg2X <= -1200:
        bg2X =1200
        bg1X = 0


    for g in goldList:
        screen.blit(gold,(g.x-25,g.y-25))
        g.x -= 3
        if g.x <= -50:
            goldList.remove(g)
            del(g)    

    for s in silverList:
        screen.blit(silver,(s.x-25,s.y-25))
        s.x -=3 
        if s.x <= -50:
            silverList.remove(s)
            del(s)
    
    # if gX <= -50:
    #     gX =  1300
    #     gY =  random.randint(300,490)
    # if sX <= -50:
    #     sX =  random.randint(100,1200)
    #     sY =  random.randint(300,490)

    if cnt%3 ==0:
        screen.blit(run1,(rx-50,ry-50))
    elif cnt%3 ==1:
        screen.blit(run2,(rx-50,ry-50))   
    elif cnt%3 ==2:
        screen.blit(run3,(rx-50,ry-50))  

    if cnt%50 == 0:
        scoin()
    if cnt%100 == 0:
        gcoin()

    for g in goldList:
        result = collision(g.x,g.y,rx,ry)
        if result == 1:
            g.x = 1500
            goldList.remove(g)
            del(g)
            score += 100
    for s in silverList:
        result = collision(s.x,s.y,rx,ry)
        if result ==1:
            s.x = 1500
            silverList.remove(s)
            del(s)
            score += 50
            
    
    txt = myFont.render("SCORE :" + str(score), False, (255,0,0))
    screen.blit(txt,(550,60))
    


    pygame.display.update()

pygame.quit()