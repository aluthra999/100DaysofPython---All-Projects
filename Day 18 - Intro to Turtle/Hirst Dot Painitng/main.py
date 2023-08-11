# import colorgram
import turtle as t
import random

# TODO part 1 - Extracting Colors only RGB numbers
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

# TODO : part 2 making dot painting
# making dot painting in turtle using the color_list extracted with colorgram in part 1

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
# change starting position
chaining_position = -200


def moving():
    tim.speed(0)
    tim.goto(-250, chaining_position)


moving()
for x in range(10):
    for y in range(10):
        tim.speed(0)
        tim.dot(15, random.choice(color_list))
        tim.forward(50)
    chaining_position += 50
    moving()

screen = t.Screen()
screen.exitonclick()
