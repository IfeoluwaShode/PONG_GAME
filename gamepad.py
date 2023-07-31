from turtle import Turtle
class Gamepad(Turtle):
    def __init__(self, location):
        self.location = location
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(location)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_back(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)