from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pad1 = Paddle((350, 0))
pad2 = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
screen.onkey(pad2.up, "w")
screen.onkey(pad2.down, "s")
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(pad1) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.points_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.points_r()











screen.exitonclick()
