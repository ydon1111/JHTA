from turtle import*
from random import*



a = Turtle()
screen = Screen()
print(a)
print(screen)

screen.addshape("audience.gif")
screen.addshape("turtle.gif")
a.shape("audience.gif")
a.penup()
a.goto(0,260)

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-400,0)
t1.pendown()
t1.write("1번")

t2 = Turtle()
t2.color('blue')
t2.shape('turtle')
t2.penup()
t2.goto(-400,-30)
t2.pendown()
t2.write("2번")

t3 = Turtle()
t3.color('green')
t3.shape('turtle')
t3.penup()
t3.goto(-400,-60)
t3.pendown()
t3.write("3번")


t4 = Turtle()
t4.color('purple')
t4.shape('turtle')
t4.penup()
t4.goto(-400,-90)
t4.pendown()
t4.write("4번")


t5 = Turtle()
t5.color('orange')
t5.shape('turtle')
t5.penup()
t5.goto(-400,-120)
t5.pendown()
t5.write("5번")


b = Turtle()
b.color("black")
b.penup()
b.goto(-380,90)
b.pendown()
b.rt(90)
b.fd(300)
b.speed(10)


for i in range(4):
    b.penup()
    b.lt(90)
    b.fd(90)
    b.lt(90)
    b.pendown()
    b.fd(300)
    b.penup()
    b.rt(90)
    b.fd(90)
    b.rt(90)
    b.pendown()
    b.fd(300)

b.penup()
b.fd(10000)

n = textInput("골라",'어떤거북이를 고르실건가요?')
a.color("red")
a.write(n+"번 거북이 이겨라!!")

dis1 = 0 
dis2 = 0 
dis3 = 0 
dis4 = 0 
dis5 = 0 
for i in range(250):
    rnd1 = randint(1,5)
    rnd2 = randint(1,5)
    rnd3 = randint(1,5)
    rnd4 = randint(1,5)
    rnd5 = randint(1,5)
    dis1 += rnd1
    dis2 += rnd2
    dis3 += rnd3
    dis4 += rnd4
    dis5 += rnd5
    t1.fd(rnd1)
    t2.fd(rnd2)
    t3.fd(rnd3)
    t4.fd(rnd4)
    t5.fd(rnd5)
    
    if dis1 >=725:
        t1.penup()
        t1.goto(0,100)
        t1.pendown()
        t1.shape("turtle.gif")
        break
    elif dis2 >=725:
        t2.penup()
        t2.goto(0,100)
        t2.pendown()
        t2.shape("turtle.gif")
        break
    elif dis3 >=725:
        t3.penup()
        t3.goto(0,100)
        t3.pendown()
        t3.shape("turtle.gif")       
        break
    elif dis4 >=725:
        t4.penup()
        t4.goto(0,100)
        t4.pendown()
        t4.shape("turtle.gif")      
        break
    elif dis5 >=725:
        t5.penup()
        t5.goto(0,100)
        t5.pendown()
        t5.shape("turtle.gif")       
        break
    





mainloop()

