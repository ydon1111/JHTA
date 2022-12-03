import turtle as t 
import math
tm = 0.3
ux = 3
uy =0
dx =0
dy =0
g = 9.8
velo = 0
ang = 0

def draw_pos(x,y):
    velo = t.numinput("입력","속도:",50,10,100)
    ang = math.radians(t.numinput("입력","각도:",45,0,360))
    t.clearstamps()
    t.up()
    t.setpos(x,y)
    t.down()
    t.stamp()
    hI = -t.window_height() /2 
    ux = velo*math.cos(ang)
    uy = velo*math.sin(ang)
    while True:
        uy = uy + (-1*g)*tm
        dy = t.ycor()+(uy*tm)-(g*tm**2)/2
        dx = t.xcor() + (ux*tm)
        if dy > hI:
            t.goto(dx,dy)
            t.stamp()
        else:
            break

draw_pos(-100,100)
t.done()