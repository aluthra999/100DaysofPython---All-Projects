from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.SCORE_R = 0
        self.SCORE_L = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.SCORE_R}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.SCORE_L}", move=False, align=ALIGNMENT, font=FONT)

    def l_update(self):
        self.SCORE_L += 1

    def r_update(self):
        self.SCORE_R += 1

