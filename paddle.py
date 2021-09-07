from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xy):
        super().__init__()
        self.createPaddle(xy)

    def createPaddle(self,xy):
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(xy)

    def goUP(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def goDOWN(self):
        self.goto(self.xcor(), (self.ycor() - 20))
