from turtle import Turtle

# dictionary - key: pressure, value: list of (1) colour, (2) radius of circle (3) amounts of circles
strength_dictionary = {
    1: ["bisque", 10, 1],
    2: ["peach puff", 20, 2],
    3: ["light salmon", 30, 3],
    4: ["tomato", 40, 4],
    5: ["orange red", 50, 5],
    6: ["red", 60, 6],
    7: ["crimson", 70, 7],
    8: ["brown", 80, 8],
    9: ["dark red", 90, 9],
    10: ["maroon", 100, 10],
}


class Circle(Turtle):

    def __init__(self, position, pressure):
        super().__init__()
        # preparing the turtle:
        self.width(4)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()

        # getting the colour right:
        pressure_color = (strength_dictionary[pressure])[0]
        self.color(pressure_color)
        self.draw_circle(pressure)

    def draw_circle(self, pressure):

        # determining the amount of circles based on pressure
        amount_of_circles = (strength_dictionary[pressure])[2]

        # starting_radius = where all circles start, pressure_radius = biggest radius of the circle that is to be drawn
        starting_radius = 10
        pressure_radius = (strength_dictionary[pressure])[1]

        # draw circle by circle. starting from smallest radius and increasing until pressure_radius is reched
        for circle in range(amount_of_circles):
            if starting_radius <= pressure_radius:
                self.circle(starting_radius)
                starting_radius += 10
                # moving turtle down by 10px so all circles have the same midpoint
                self.penup()
                self.setheading(270)
                self.forward(10)
                self.setheading(0)
                self.pendown()

                # removing previous circle after drawing it
                self.clear()

        # correcting the surplus movement down of the turtle during the last circle
        self.penup()
        self.setheading(90)
        self.forward(15)
        self.setheading(0)
        self.pendown()

        # circle moving inwards again
        while starting_radius > 0:
            self.circle(starting_radius-15)
            starting_radius -= 10
            self.penup()
            self.setheading(90)
            self.forward(10)
            self.setheading(0)
            self.pendown()

            # removing previous circle after drawing it
            self.clear()
