from turtle import Turtle

class Snake:
    def __init__(self):
        self.all_segments = []
        self.x_cord = 0
        self.create_snake()

    def create_snake(self):
        for _ in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            # new_segment.speed("fastest")
            new_segment.goto(x=self.x_cord, y=0)
            self.x_cord -= 20
            self.all_segments.append(new_segment)

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.all_segments[-1].position())
        self.all_segments.append(new_segment)

    def move(self):
        for turtle_no in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[turtle_no - 1].xcor()
            new_y = self.all_segments[turtle_no - 1].ycor()
            self.all_segments[turtle_no].goto(new_x, new_y)

        self.all_segments[0].forward(20)

    def up(self):
        if self.all_segments[0].heading() != 270:
            self.all_segments[0].setheading(90)

    def down(self):
        if self.all_segments[0].heading() != 90:
            self.all_segments[0].setheading(270)

    def left(self):
        if self.all_segments[0].heading() != 0:
            self.all_segments[0].setheading(180)

    def right(self):
        if self.all_segments[0].heading() != 180:
            self.all_segments[0].setheading(0)