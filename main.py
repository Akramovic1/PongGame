from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from line import Line


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Line()
screen.listen()
screen.onkey(r_paddle.goUP, "Up")
screen.onkey(r_paddle.goDOWN, "Down")
screen.onkey(l_paddle.goUP, "w")
screen.onkey(l_paddle.goDOWN, "s")
game_is_on = True

while game_is_on:

    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 55 and 330 < ball.xcor() < 350 \
            or ball.distance(l_paddle) < 55 and -350 < ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.r_point()

screen.exitonclick()