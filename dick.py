from turtle import Turtle


class Dick(Turtle):

    def __init__(self):
        super().__init__()
        # preparing the turtle:
        self.hideturtle()
        self.speed(0)
        self.goto(-700, -100)
        self.color("white")

        # drawing the d
        self.draw_dick()

    def draw_dick(self):
        self.setheading(270)
        self.circle(100, 180)
        self.setheading(0)
        self.forward(750)
        self.setheading(0)
        self.circle(100, 180)
        self.forward(750)
        self.setheading(90)
        self.circle(100, 180)
