from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
ADVANCE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle('square')
            if i == 0:
                new_segment.color('orange')
            else:
                new_segment.color('white')
            new_segment.penup()
            new_segment.goto(STARTING_POSITIONS[i])
            self.segments.append(new_segment)

    def extend_snake(self):
        extra_segment = Turtle('square')
        extra_segment.color('white')
        extra_segment.penup()
        extra_segment.goto(self.segments[-1].position())
        # add it to the position of the last segment.
        self.segments.append(extra_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.fd(ADVANCE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # to go off the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
