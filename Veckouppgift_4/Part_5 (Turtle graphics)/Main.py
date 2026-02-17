#Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
#forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
#backward - gå bakåt
#left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
#dot - sätt ut en prick med en viss storlek
#speed - normal=6, fast=10, maximal=0

import turtle as t, math

#triangle
def paint_triangle(side,color="black"):
    t.color(color)
    for x in range(3):
        t.forward(side)
        t.left(120)

#square
def paint_Square(side,color="black"):
    t.color(color)
    for x in range(4):
        t.forward(side)
        t.left(90)

#cirkel
def paint_circle(r, color="black", degrees=360, direction="left"):
    t.color(color)
    for x in range(degrees):
        if direction=="left":
            t.left(1)
        else:
            t.right(1)
        t.forward(r*2*math.pi/360)


paint_triangle(120, "blue")

t.penup()
t.forward(200)
t.dot(10,"red")
t.color("blue")
t.forward(50)
t.pendown()

paint_Square(100, "yellow")

o=1000
r=o/(2*math.pi)

t.speed(0)
t.penup()
t. left(180)
t.forward(50)
t.right(90)
t.forward(r)
t.left(90)
t.pendown()

paint_circle(r)

t.penup()
t.right(90)
t.forward(20)
t.left(90)
t.pendown()
t.color("green")
t.circle(r+20)


#Bokstäverna i ordet python
t.penup()
t.goto(-50,0)
t.pendown()
t.write("PYTHON")




text_height=20
color = "red"
t.color(color)

t.penup()
t.goto(-text_height*6,100)
baseCor = t.ycor()
t.pendown()


#P
t.right(90)
t.forward(text_height)
t.right(90)
t.forward(text_height*0.3)
paint_circle(text_height*0.25,color,180,"right")
t.forward(text_height*0.3)

#space
t.penup()
t.goto(t.xcor()+1.1*text_height,baseCor)
t.pendown()

#Y
t.right(90)
t.forward(text_height*0.5)
t.goto(t.xcor()-text_height*0.5,t.ycor()+text_height*0.5)
t.penup()
t.goto(t.xcor()+text_height,t.ycor())
t.pendown()
t.goto(t.xcor()-text_height*0.5,t.ycor()-text_height*0.5)

#space
t.penup()
t.goto(t.xcor()+text_height*1.1,baseCor)
t.pendown()

#T
t.goto(t.xcor(),t.ycor()+text_height)
t.goto(t.xcor()-text_height*0.5,t.ycor())
t.goto(t.xcor()+text_height,t.ycor())

#H
t.goto(t.xcor(),t.ycor()-text_height)
t.goto(t.xcor(),t.ycor()+text_height*0.5)
t.goto(t.xcor()+text_height,t.ycor())
t.goto(t.xcor(),t.ycor()+text_height*0.5)
t.goto(t.xcor(),t.ycor()-text_height)

#space
t.penup()
t.goto(t.xcor()+text_height*0.6,baseCor)
t.pendown()

#O
t.right(90)
paint_circle(text_height*0.5,"red")

#space
t.penup()
t.goto(t.xcor()+text_height*0.6,baseCor)
t.pendown()

#N
t.goto(t.xcor(),baseCor+text_height)
t.goto(t.xcor()+text_height,baseCor)
t.goto(t.xcor(),baseCor+text_height)

t.mainloop()