from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        x_place = randint(-280, 280)
        y_place = randint(-280, 270)
        self.goto(x_place, y_place)

