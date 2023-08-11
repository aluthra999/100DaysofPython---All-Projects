# TODO import required libraries
import turtle
import pandas as pd

# TODO Screen module setup
screen = turtle.Screen()
screen.title("U.S. State Game")
screen.setup(width=738, height=500)

# TODO convert image into shape to use as bg to do that we need to convert image to string
bg_turtle = turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
bg_turtle.penup()
bg_turtle.goto(0, 0)
bg_turtle.shape(image)


# TODO read csv file and convert the state row into list
data = pd.read_csv("50_states.csv")

state_list = data.state.to_list()


# TODO check if user guessed the right state
answer_list = []
while len(answer_list) < 50:
    # TODO ask user for an answer
    user_answer = screen.textinput(title=f"{len(answer_list)}/50 States answered", prompt="Guess a State of America.") \
        .title()

    if user_answer == "Exit":
        break
    if user_answer in state_list:
        answer_list.append(user_answer)
        state_list.remove(user_answer)
        state_data = data[data.state == user_answer]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x=state_x, y=state_y)
        state_turtle.write(arg=f"{user_answer}", font=('Arial', 8, 'normal'))

turtle.mainloop()
