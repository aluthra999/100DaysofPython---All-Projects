from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # x = 0.00
        # y = 0.00
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """It will create 3 square each at -20 to form a snake using add_segment method"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        """It will move the snake continuously in the direction where the snake head is."""
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """It will move the snake head to 90-degree(⬆) angle"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """It will move the snake head to 270-degree(⬇) angle"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """It will move the snake head to 180-degree(⬅) angle"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """It will move the snake head to 0-degree(➡) angle"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
