import pygame
import random
import math
import random

pygame.init()

screen_width =1200
screen_height = 800

#배경 이미지 객체
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")
bg = pygame.transform.scale(bg,(1200,800))

#볼 객체 
ball = pygame.image.load("e:/dev/python_workspace/img/img/gold.png")
ball = pygame.transform.scale(ball,(100,100))

#바 객체 
player = pygame.image.load("e:/dev/python_workspace/img/bar.png")
player = pygame.transform.scale(player,(300,50))

#블럭 객체 
blockblock = pygame.image.load("e:/dev/python_workspace/img/block.png")
blockblock = pygame.transform.scale(blockblock,(100,100))


# blockList = []
# def makeBlock():
#     b = Block(random.randint(1,1100),random.randint(1,600),1)
#     blockList.append(b)

def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))


def ballcollision(x1,y1,x2,y2):
    global inc_x ,inc_y
    dis = pythagoras(x1,y1,x2,y2)
    if dis < 120:
        inc_y = -inc_y
        inc_x = -inc_x
    return inc_y, inc_x


def collision(x1,y1,x2,y2):
    global inc_y,inc_x
    dis = pythagoras(x1,y1,x2,y2)
    if dis < 120:
        print("벽돌 담")
        inc_y = -inc_y
        inc_x = -inc_x
        x2 = -300
        y2 = -300
    return x2, y2 ,inc_y ,inc_x
  

def changeDirection(x,y,ix,iy):
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정
    if y <=0 or y >1100 :
        iy = -iy 
    if x <=0 or x >=1130:
        ix = -ix
    
    # elif x <= 3: 
    #     ix = -ix
    # elif x <= 1100:
    #     ix = -ix
    
    return ix,iy


class Block:
    def __init__(self,x,y,hp):
        self.x = x
        self.y = y 
        self.hp =hp
    
    def __del__(self):
        print("벽부셔짐")






screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("핑퐁")




bx = 300
by = 300

px = 600
py = 700

inc_x =random.randint(-10,10)
inc_y =random.randint(-10,10)

rx = 10
ry = 30


clock = pygame.time.Clock()





cnt = 0 
isRunning = True 
while isRunning:
    bx -= inc_x 
    by -= inc_y
    cnt +=1
    fps = clock.tick(30)  #화면의 프레임수 

    inc_x ,inc_y = changeDirection(bx,by,inc_x,inc_y)
    ballcollision(px,py,bx,by)
   
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 

    if keys[pygame.K_RIGHT] == 1:
        px += 10
        if px >1030:
            px =1030

    if keys[pygame.K_LEFT] ==1:
        px -= 10
        if px <60:
            px =60

    # if cnt%30 == 0:
    #     makeBlock()
    
 
    
    
    


    screen.blit(bg,(0,0))
    screen.blit(ball,(bx-50,by-50))
    screen.blit(player,(px-150,py-25))
    

   
    # for m in blockList:
    #     result = collision(m.x,m.y,bx,by)
    #     if result ==1:
    #         m.hp -=1 
    #         inc_y = -inc_y
    #         inc_x = -inc_x
    #     if m.hp <= 0 :
    #         m.x = -950
    #         blockList.remove(m)
    #         del(m) 
   
        
    # for i in range(4):
    #     for k in range(10):
    #         screen.blit(blockblock,(rx+100*k,ry*i))
    #     ry=100
    screen.blit(blockblock,(rx+100,ry))
    collision(bx,by,rx,ry)   

    pygame.display.update()
   

pygame.display.update()

pygame.quit()