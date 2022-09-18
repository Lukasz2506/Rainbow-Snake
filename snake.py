from turtle import Turtle
from colors import rain_colors
from random import randint

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LIMIT_VALUE = 280




class Snake:

    def __init__(self):
        self.snake_seg = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_seg = Turtle(shape="square")
        snake_seg.color(rain_colors[randint(0, 6)])
        snake_seg.penup()
        snake_seg.goto(position)
        self.segments.append(snake_seg)

    def new_segment(self):
        self.add_segment((self.segments[-1].xcor()+20, self.segments[-1].ycor()+20))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(LEFT)