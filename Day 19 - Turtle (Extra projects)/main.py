# TODO Rainbow HEX-Spiral
# import turtle
# from turtle import Turtle, Screen
# import colorsys
#
# t = Turtle()
# s = Screen().bgcolor('black')
# t.color('white')
# t.speed(0)
# t.width(5)
#
# n = 200
# h = 0
#
# for i in range(200):
#     t.right(59)
#     for c in range(1):
#         t.forward(i*2)
#         c = colorsys.hsv_to_rgb(h,1,0.8)
#         h += i/n
#         t.color(c)
#
# turtle.exitonclick()


# TODO Virus design
# from turtle import *
# speed(10)
# color("cyan")
# bgcolor('black')
# b = 200
# while b > 0:
#     left(b)
#     forward(b*3)
#     b -= 1


# TODO Spiral of Square I
# from turtle import *
#
# speed(0)
# bgcolor('black')
# pencolor('white')
# for i in range(10, 240):
#     for j in range(4):
#         fd(i)
#         right(90)
#     right(10)
#
# done()

# TODO Spiral of Square II
# import turtle
#
# a = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor('black')
# col = ('white', 'orange', 'red', 'yellow', 'green', 'blue', 'cyan')
# a.speed(0)
#
# for i in range(200):
#     a.forward(i*4)
#     a.right(91)
#     a.color('white')
#     for b in range(3):
#         a.forward(i*4)
#         a.right(91)
#         for с in range(2):
#             a. forward(i*4)
#             a.right(91)

# TODO Cross filled
# from turtle import Turtle, Screen
#
# t = Turtle()
# s = Screen()
#
# t.begin_fill()
# for i in range(4):
#     t.fd(100)
#     t.lt(90)
#     for j in range(4):
#         t.fd(100)
#         t.rt(90)
# t.end_fill()

# s.exitonclick()
