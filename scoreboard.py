from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_chart()

    def score_chart(self):
        self.goto(0, 260)
        self.write(f"{self.left_score} Score {self.right_score}", align=ALIGNMENT, font=FONT)

    def points_l(self):
        self.left_score += 1
        self.clear()
        self.score_chart()

    def points_r(self):
        self.right_score += 1
        self.clear()
        self.score_chart()
