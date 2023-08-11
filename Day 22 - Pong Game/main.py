from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PyPong")

# Right paddle
r_paddle = Paddle()
r_paddle.create_paddle(350, 0, 'blue')
screen.onkey(r_paddle.paddle_up, 'Up')
screen.onkey(r_paddle.paddle_down, 'Down')

# Left paddle
l_paddle = Paddle()
l_paddle.create_paddle(-350, 0, 'gold')
screen.onkey(l_paddle.paddle_up, 'w')
screen.onkey(l_paddle.paddle_down, 's')


screen.listen()
screen.tracer(0)

ball = Ball()
score = Score()


game_is_on = True
i = 0
while game_is_on:
    i += 1
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.r_update()
        score.update_score()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.l_update()
        score.update_score()

screen.exitonclick()
