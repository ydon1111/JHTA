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


blockList = []
def makeBlock():
    bx = 300
    by = 100
    for i in range(3):
        temp_list = []
        for j in range(5):
            temp_list.append(Block(bx,by,1))
            bx += 150
        blockList.append(temp_list)
        bx = 300
        by += 120

def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

def ballcollision(x1,y1,x2,y2):
    global inc_y
    dis = pythagoras(x1,y1,x2,y2)
    if dis < 110:
        inc_y = -inc_y  
    return inc_y

def collision(x1,y1,x2,y2):
    dis = pythagoras(x1,y1,x2,y2)
    result = 0   
    if dis <120:
        result=1
    return result

def changeDirection(x,y,ix,iy):
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정
    if y <=0 or y >1100 :
        iy = -iy 
    if x <=0 or x >=1130:
        ix = -ix
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

bx = 1000
by = 300

px = 600
py = 700

inc_x =random.randint(-10,10)
inc_y =random.randint(-10,10)
clock = pygame.time.Clock()

cnt = 0 
isRunning = True 
makeBlock()
while isRunning:
    bx -= inc_x 
    by -= inc_y
    cnt +=1
    fps = clock.tick(60)  #화면의 프레임수 

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

    screen.blit(bg,(0,0))
    screen.blit(ball,(bx-50,by-50))
    screen.blit(player,(px-150,py-25))
    

   
    for i, m in enumerate(blockList):
        for n in m:
            result = collision(n.x,n.y,bx,by)
            if result ==1:
                n.hp -=1 
                inc_y = -inc_y
                inc_x = -inc_x
            if n.hp <= 0 :
                n.x = -950
                blockList[i].remove(n)
                del(n) 
   
   
    for s_list in blockList:
        for s in s_list:
            screen.blit(blockblock,(s.x-25,s.y-25))
   
    pygame.display.update()
   

pygame.display.update()

pygame.quit()




# blist = []
# #[[a,a,a,a,a],[a,a,a,a,a],[a,a,a,a,a]]
# for i in range(3):
#     temp_list = []
#     for j in range(5):
#         temp_list.append(j)
#         #[1,2,3,4,5]
#     blist.append(temp_list)
#     #[[1,2,3,4,5]]
    
# for list1 in blist:
#     #[1,2,3,4,5]
#     for a in list1:
#         screen.blit(a.img, (a.x, a.y))


