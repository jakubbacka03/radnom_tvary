import turtle
import random
t = random.Random()

def stvorec(velkost):
     for i in range(4):
         t.fd(velkost)
         t.rt(90)

def trojuholnik(velkost):
    for i in range(3):
        t.fd(velkost)
        t.lt(120)

def rozmiestnenie():
    t.pu()
    t.setpos(random.randrange(-200, 200), random.randrange(-200, 200))
    t.seth(random.randrange(360))
    t.pd()

turtle.delay(0)
t = turtle.Turtle()
t.pensize(5)
for i in range(20):
    rozmiestnenie()
    if random.randrange(2):
        t.pencolor('blue')
        stvorec(40)
    else:
        t.pencolor('red')
        trojuholnik(40)
turtle.exitonclick()