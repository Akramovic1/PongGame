from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.goUP, "Up")
screen.onkey(r_paddle.goDOWN, "Down")
screen.onkey(l_paddle.goUP, "w")
screen.onkey(l_paddle.goDOWN, "s")
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()