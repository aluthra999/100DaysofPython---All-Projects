# TODO Turtle Project
from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
# print(timmy)


# timmy.shape("turtle")
# shape could be any one of this:- "arrow", "turtle", "circle", "square", "triangle", "classic"

# timmy.color('pink')
# color have a wide range of variety and right name can be found online @ cs111 turtle color.
# timmy.color("color1", "color2")

# TODO - Draw a Square
# --------------------------- ###
#         Lecture 166         ###
#       (Draw a Square)       ###

# for x in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# TODO - Draw a Dotted Line
# --------------------------- ###
#          Lecture #168       ###
#       (Draw a dotted line)  ###

# for number in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# TODO - Draw different shapes 1.0
# --------------------------- ###
#    Lecture #169 - Version 1 ###
# (Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon)      ###

# change starting position
# timmy.penup()
# timmy.setpos(-50, 80)
# timmy.pendown()


# color
# def color():
#     color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "cyan"]
#     random_color = random.choice(color_list)
#     timmy.color(random_color)


# triangle
# def triangle():
#     color()
#     for _ in range(3):
#         timmy.forward(100)
#         timmy.left(-120)
#     timmy.forward(100)


# square
# def square():
#     color()
#     for _ in range(4):
#         timmy.left(-90)
#         timmy.forward(100)


# pentagon
# def pentagon():
#     color()
#     for _ in range(5):
#         timmy.left(-72)
#         timmy.forward(100)


# hexagon
# def hexagon():
#     color()
#     for _ in range(6):
#         timmy.left(-60)
#         timmy.forward(100)


# heptagon
# def heptagon():
#     color()
#     for _ in range(7):
#         timmy.left(-51.42)
#         timmy.forward(100)


# octagon
# def octagon():
#     color()
#     for _ in range(8):
#         timmy.left(-45)
#         timmy.forward(100)


# nonagon
# def nonagon():
#     color()
#     for _ in range(9):
#         timmy.left(-40)
#         timmy.forward(100)


# decagon
# def decagon():
#     color()
#     for _ in range(10):
#         timmy.left(-36)
#         timmy.forward(100)


# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()


# TODO - Draw different shapes 2.0
# -------------------------------------------- ###
# Lecture #169 - Version 2 (shorter & simpler) ###
# (Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon)      ###

# num_sides = 2
#
# for _ in range(8):
#     num_sides += 1
#     color()
#     for x in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.left(-angle)


# TODO - Generate a random walk
# ------------------------------- ###
#          Lecture #170           ###
#       (Generate a random walk)  ###

# timmy.speed(6)
# timmy.pensize(1)


# Define a function for a single step of the walk
# def take_step():
#     direction = random.choice([0, 90, 180, 270])
#     distance = random.randint(10, 50)
#     timmy.setheading(direction)
#     timmy.forward(distance)


# Take 100 steps of the walk
# for i in range(200):
#     color()
#     take_step()


# TODO - Tuples and How to Generate Random RGB Colours
# ------------------------------- ###
#          Lecture #171           ###
#    (Generate random RGB color)  ###

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour
#
#
# direction = [0, 90, 180, 270]
# timmy.speed(6)
# timmy.pensize(1)
#
# # Take 100 steps of the walk
# for i in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))
#


# TODO - Draw a Spirograph
# ------------------------------- ###
#          Lecture #172           ###
#       (Draw a Spirograph)       ###

# # some code from ChatGPT + self edited start
# t.speed("fastest")
#
# for i in range(72):
#     t.color(random_color())
#     t.circle(100)
#     t.left(5)
# # some code from ChatGPT + self edited end


# Code from class
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size_of_gap)
#
#
# draw_spirograph(5)


# TODO - "The Hirst Painting Project", How to extract RGB Values from Images
# -------------------------------  ###
#          Lecture #173            ###
# (Extract RGB Values from Images) ###


# Display Screen
# screen = Screen()
# screen.exitonclick()
