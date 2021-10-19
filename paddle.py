from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cor_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(cor_pos)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
