import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# starting position of turtle at x-axis
x = -230

# starting position of turtle at y-axis
if len(color) >= 8:
    y = -170
elif len(color) >= 14:
    screen.textinput(title='Over Crowded!!!', prompt='Max 13 turtles can participate at once.')
else:
    y = -70


all_turtle = []

for turtle_index in range(0, len(color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 30
    all_turtle.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win!, The {winning_color} turtle is the winner")
            else:
                print(f"You lost!, The {winning_color} turtle is the winner")
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
