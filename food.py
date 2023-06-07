from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # the default size for the circle is (20 * 20)
        # stretch len and width to the half of its size using shapesize.
        self.color('blue')
        self.speed("fastest")
        self.refresh()

    def refresh(self): # refresh the food when snake collide with it.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
