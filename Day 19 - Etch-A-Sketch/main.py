from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.color("red")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def face_right():
    tim.right(90)


def face_left():
    tim.left(90)


def circle():
    tim.circle(10)


def fly_forward():
    tim.speed(0)
    tim.forward(50)


def fly_backward():
    tim.speed(0)
    tim.forward(-50)


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="r", fun=tim.reset)
screen.onkey(key="a", fun=face_left)
screen.onkey(key="d", fun=face_right)
screen.onkey(key="w", fun=fly_forward)
screen.onkey(key="s", fun=fly_backward)
screen.onkey(key="8", fun=tim.penup)
screen.onkey(key="2", fun=tim.pendown)
screen.onkey(key="c", fun=circle)
screen.exitonclick()
