import turtle as t 
t.shape('turtle')
t.color("deepskyblue")


for i in range(4):
    t.forward(100)
    t.right(90)
    
# t.rt
# t.lt
# t.fd

t2 = t.Pen()
t2.shape("turtle")
t2.color("#ff6600")
t2.penup()
t2.goto(-200,100)
t2.pendown()
t2.begin_fill()
t2.fillcolor("#ff6600")
t2.circle(25) #반지름
t2.end_fill()

t3 = t.Pen()
t3.shape('turtle')
t3.shapesize(5)
t3.color("red")


t3.penup()
t3.goto(100,100)
t3.pendown()
for i in range(5):
    t3.fd(100)
    t3.rt(72)


t4 = t.Pen()
t4.shape('turtle')
t4.penup()
t4.goto(200,100)
t4.pendown()
t4.circle(20,100) #100도만큼만 그림


t.mainloop()
