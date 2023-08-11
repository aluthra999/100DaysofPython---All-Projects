# TODO import required libraries
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's the state's name? ").title()
    # print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        t.goto(state_x, state_y)
        t.write(state_data.state.item())


not_answered = pandas.DataFrame(all_states)
not_answered.to_csv('states_to_learn.csv')
