from cgitb import reset
from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((370, 0))
left_paddle = Paddle ((-370, 0))

game_ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_ball.move()

    # Detect collision with wall
    if game_ball.ycor() > 282 or game_ball.ycor() < -282:
        game_ball.bounce_y()

    # Detect collision with right_paddles
    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 340 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -340:
        game_ball.bounce_x()

    # Detect when right paddle misses
    if game_ball.xcor() > 390:
        time.sleep(1.5)
        game_ball.reset_position()

    # Detect when left paddle misses
    if game_ball.xcor() < -390:
        time.sleep(1.5)
        game_ball.reset_position()



screen.exitonclick()