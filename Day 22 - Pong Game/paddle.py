from turtle import Turtle
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self, goto_x, goto_y, color):
        """It will create a paddle, 1st argument is 'goto' it needs the number where you want your paddle
        on x-axis, fill the number according to screen size. On a width of 800, anywhere between 350-370 works
        fine. 2nd argument is 'color', you can select your own paddle color."""
        self.penup()
        self.speed(0)
        self.goto(goto_x, goto_y)
        self.color(color)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def paddle_up(self):
        if self.ycor() < 230:
            self.sety(self.ycor() + MOVEMENT)

    def paddle_down(self):
        if self.ycor() > -230:
            self.sety(self.ycor() - MOVEMENT)

