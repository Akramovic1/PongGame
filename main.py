from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle = Paddle()
screen.listen()
screen.onkey(paddle.goUP, "Up")
screen.onkey(paddle.goDOWN, "Down")
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()