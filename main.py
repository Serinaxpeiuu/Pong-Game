from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE_L_POS = (-350, 0)
PADDLE_R_POS = (350, 0)
LEFT_SCORE_POS = (-30, 250)
RIGHT_SCORE_POS = (30, 250)

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor((0, 102, 204))
screen.title("Pong Game🏓")
screen.tracer(0)  # 0 to turn off the animation
screen.mode("standard")

paddle_l = Paddle(PADDLE_L_POS)
paddle_r = Paddle(PADDLE_R_POS)
score_l = ScoreBoard(LEFT_SCORE_POS)
score_r = ScoreBoard(RIGHT_SCORE_POS)
ball = Ball()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_pace)
    ball.move()

    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect out-of-range
    else:
        if ball.xcor() > 380:
            ball.reset_position()
            score_l.increase_score()

        elif ball.xcor() < -380:
            ball.reset_position()
            score_r.increase_score()

screen.exitonclick()
