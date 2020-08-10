import pygame
import math
import random

pygame.init()
# pygame.mixer.init()


#토끼의 중심좌표와 마우스 클릭 위치의 거리를 구하기 

def pythagoras (x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))



screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))

#배경그리기
bg1 = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
bg2 = pygame.image.load('e:/dev/python_workspace/img/img/bg.jpg')
#배경 사이즈 조절 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))

#조준경 
snipe = pygame.image.load('e:/dev/python_workspace/img/img/snipe.png')
snipe = pygame.transform.scale(snipe,(100,100))
#홀 
hole = pygame.image.load('e:/dev/python_workspace/img/img/hole.png')
hole = pygame.transform.scale(hole,(10,10))



#토끼 그리기 
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/img/rabbit2.png')
#토끼 사이즈 조절
rabbit1 = pygame.transform.scale(rabbit1,(100,100))
rabbit2 = pygame.transform.scale(rabbit2,(100,100))
#시계변수
clock = pygame.time.Clock()

#배경음악 삽입
# pygame.mixer.music.load('e:/dev/python_workspace/sounds/backsound.mp3')
# pygame.mixer.music.set_volume(1) # 1~0.1
# pygame.mixer.music.play(1)


#특정 사운드 객체
# 총소리
# fsound = pygame.mixer.sound('e:/dev/python_workspace/sounds/fire.wav')
# fsound.set_volume(1)

#맞은소리
# ssound = pygame.mixer.sound('e:/dev/python_workspace/sounds/scream.wav')
# ssound.set_volume(1)


isRunning = True #게임을 계속 진행할지 , 중지 할지를 결정하는 변수 
pygame.display.set_caption("토끼 사냥")

#토끼 시작좌표 
rx = 100
ry = 200

#배경 좌표
bg1X = 0 
bg2X = 1200 

#조준경 좌표
snipeX = 300
snipeY = 300

#홀 좌표
holeX = 300
holeY = 300

#hole 리스트 

holeList = []

#반동
rebound = 0

# 폰트 설정 
pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS",30)


# 점수판 
score = 0


cnt = 0 
while isRunning:
    cnt += 1 
    bg1X -=1
    bg2X -=1 

    fps = clock.tick(120) #화면의 초당 프레임수 60

    #프레임이 얼마 인지 확인
    # print("fps :"+ str(clock.get_fps()))

    if rebound > 2:
        rebound -= 2


    for event in pygame.event.get():  #이벤트 모으기 
        if event.type == pygame.QUIT:
            isRunning = False
        # print(keys[pygame.K_LEFT])
   
        if event.type == pygame.MOUSEBUTTONUP:
            rebound=50 
            # fsound.play()
            holeX,holeY = pygame.mouse.get_pos()
            dis = pythagoras(holeX,holeY,rx+50,ry+50)
            # print(dis)
            
            
            if dis <= 40:
                print("맞음")
                # ssound.play()
                holeList.append((rx+50-holeX,ry+50-holeY))
                rx= random.randint(10,1100)
                ry= random.randint(10,700)
                score += 100
            #만약 dis 의 작으면 맞은것 
            #크면 맞은것 
    # print("홀리스트: ",holeList)        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] == 1:  #왼족 화살표 버튼이 눌리면상태면 
        rx -= 5  
        if rx<0:
            rx=0            
    if keys[pygame.K_RIGHT] ==1:
        rx += 5 
        if rx>1100:
            rx= 1100
    if keys[pygame.K_UP] == 1:       
        ry -= 5 
        if ry < 0:
            ry =0       
    if keys[pygame.K_DOWN] ==1:    
        ry += 5 
        if ry > 700:
            ry = 700
     

    # 1번키를 누르면 음악 중지
    # if keys[pygame.K_1] ==1:
    #     pygame.mixer.music.stop()
    # if keys[pygame.k_2] ==1:
    #     pygame.mixer.music.play()
    # 2번키 누르면 음악 시작
        
        
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
    
    #토끼 그리기
    if  cnt%2 == 0:
        screen.blit(rabbit1,(rx,ry))
    else: 
        screen.blit(rabbit2,(rx,ry))
    

    
    # print(pygame.mouse.get_pressed())          #마우스 클릭하면 어디눌리는 구하기 

    #홀 그리기
    for holeX,holeY in holeList: 
        if len(holeList) <= 5:
            screen.blit(hole,(rx+50-holeX,ry+50-holeY))
        else:
            del holeList[0]

    # screen.blit(hole,(holeX-5,holeY-5))
    
    #조준경 그리기 
    snipeX , snipeY = pygame.mouse.get_pos()   #마우스 좌표 구하기 
    screen.blit(snipe,(snipeX-50,snipeY-50-rebound))
    # antialias <== False 
    # 화상 내의 선과 모서리를 매끄럽게 나타내는 효과 

    txt = myFont.render("SCORE :" + str(score), False, (255,0,0))
    screen.blit(txt,(550,60))

    pygame.display.update() #게임화면을 다시 그리기






pygame.quit()