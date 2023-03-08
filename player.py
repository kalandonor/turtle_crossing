from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_turtle()

    def reset_turtle(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("green")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reached_other_side(self):
        return self.ycor() >= 280

