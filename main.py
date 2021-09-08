from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.goUP, "Up")
screen.onkey(r_paddle.goDOWN, "Down")
screen.onkey(l_paddle.goUP, "w")
screen.onkey(l_paddle.goDOWN, "s")
game_is_on = True

while game_is_on:
    sleep(0.08)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()