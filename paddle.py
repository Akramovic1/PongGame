from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.createPaddle()

    def createPaddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(350, 0)

    def goUP(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def goDOWN(self):
        self.goto(self.xcor(), (self.ycor() - 20))
