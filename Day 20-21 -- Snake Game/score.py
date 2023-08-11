from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = -1
        self.count_score()

    def count_score(self):
        self.SCORE += 1
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"Score: {self.SCORE}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

