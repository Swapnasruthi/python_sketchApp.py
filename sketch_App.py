import turtle as t
tim=t.Turtle()
tim.pensize(5)
tim.speed(10)
def move_forward():
    tim.fd(20)
def move_backward():
    tim.bk(20)
def anti_clockwise():
    tim.left(15)
def clockwise():
    tim.right(15)
def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen=t.Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=anti_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=screen_clear)
screen.exitonclick()