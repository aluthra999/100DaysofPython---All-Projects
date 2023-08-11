from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# TODO Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# TODO Create snake form snake.py and initialize the keys to control the snake via methods from snake.py
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# TODO Show food on screen from food.py
food = Food()


# TODO Count score if food is eaten
score = Score()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO Detect if snake make contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count_score()

    # TODO Detect if snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # TODO Detect snake collision with tail/body
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
