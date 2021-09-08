from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, -300)
        self.goto(0, 300)