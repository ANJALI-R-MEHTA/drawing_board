import turtle as t
import random
tim=t.Turtle()
tim.width(7)
t.colormode(255)
def coloor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    coloor=(r,g,b)
    return coloor
screen=t.Screen()
screen.listen()
tim.color(coloor())
tim.write("""space=ahead,
          a=behind,
          c=clear screen,
          s=turn up
          ,d=turn down,
          w=turn left,
          x=turn right""",True,align="right")
def ahead():
    tim.forward(10)
    tim.color(coloor())
screen.onkeypress(key="space",fun=ahead)
def behind():
    tim.backward(10)
    tim.color(coloor())
screen.onkeypress(key="a",fun=behind)
def up():
    tim.setheading(90)
screen.onkey(key="s",fun=up)
def down():
    tim.setheading(270)
screen.onkey(key="d",fun=down)
def left():
    tim.setheading(180)
screen.onkey(key="w",fun=left)
def right():
    tim.setheading(0)
screen.onkey(key="x",fun=right)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.write("""space=ahead,
          a=behind,
          c=clear screen,
          s=turn up
          ,d=turn down,
          w=turn left,
          x=turn right""",True,align="right")
screen.onkey(key="c",fun=clear)



screen.exitonclick()
