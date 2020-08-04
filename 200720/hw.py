import turtle as t

t.color("green")
t.penup()
t.rt(90)
t.fd(250)
t.lt(90)
t.pendown()
t.circle(300)


t.penup()
t.color("red")
t.goto(100,50)
t.pendown()
t.circle(50)




t.penup()
t.color("red")
t.goto(100,70)

t.pendown()
t.begin_fill()
t.fillcolor("blue")
t.circle(25)
t.end_fill()





t.penup()
t.color("red")
t.goto(-100,50)
t.pendown()
t.circle(50)




t.penup()
t.color("red")
t.goto(-100,70)

t.pendown()
t.begin_fill()
t.fillcolor("blue")
t.circle(25)
t.end_fill()




t.penup()
t.color("purple")
t.goto(0,-150)

t.pendown()
t.circle(150,-80)
t.circle(150,80)
t.circle(150,80)

t.penup()
t.goto(50,-140)
t.pendown()
t.fd(-30)
t.rt(70)
t.fd(50)
t.lt(90)
t.fd(40)

t.penup()
t.goto(-50,-140)
t.pendown()
t.begin_fill()
t.fillcolor("black")
t.fd(-30)
t.lt(70)
t.fd(40)
t.rt(90)
t.fd(35)
t.end_fill()

# t.mainloop()