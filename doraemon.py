import turtle
t=turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.fillcolor("blue")
t.begin_fill()
t.circle(85)
t.end_fill()
t.penup()
t.goto(-70,40)
t.pendown()
t.left(90)
t.fillcolor("white")
t.begin_fill()
for i in range(380):
    t.forward(0.6)
    t.right(0.5)
t.end_fill()
t._rotate(-35)
t.fillcolor("white")
t.begin_fill()
for i in range(163):
    t.forward(1)
    t.right(0.62)
t.end_fill() 
t.penup()
#eye1
t.goto(30,110)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.pensize(3)
t.circle(12)
t.end_fill()
t.penup()
#eye2
t.goto(-10,110)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.pensize(3)
t.circle(12)
t.end_fill()
t.penup()
#eye1inside
t.goto(25,105)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.pensize(3)
t.circle(5)
t.end_fill()
t.penup()
#eye2inside
t.goto(-15,105)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.pensize(3)
t.circle(5)
t.end_fill()
t.penup()
t.goto(5,85)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.goto(0,75)
t.pendown()
t.left(145)
t.forward(40)
t.penup()
t.goto(15,60)
t.pendown()
t.left(90)
t.forward(40)
t.penup()
t.goto(15,75)
t.pendown()
t.left(30)
t.forward(40)
t.penup()
t.goto(15,45)
t.pendown()
t.right(60)
t.forward(40)
t.penup()
t.goto(-15,45)
t.pendown()
t.right(120)
t.forward(40)
t.penup()
t.goto(-15,60)
t.pendown()
t.right(30)
t.forward(40)
t.penup()
t.goto(-15,75)
t.pendown()
t.right(30)
t.forward(40)
t.penup()
t.goto(20,30)
t.pendown()
t.left(90)
for i in range(120):
    t.right(1)
    t.forward(0.5)
a=input("hiiii")