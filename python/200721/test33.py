import turtle as t 

t.color("red")
t.shape("turtle")
t.shapesize(1)
# t.delay(100)
t.speed(9)
t.fd(100)
dis = 100
rad =90
for i in range(50):
    dis +=5
    rad +=2
    t.rt(rad)
    t.fd(dis)


t.mainloop()