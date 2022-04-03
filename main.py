from turtle import Screen
from circles import Circle
from dick import Dick


# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1400, height=600)
screen.title("EO Data Visualization V1")

# drawing the d
dick = Dick()

# creating various different objects from the library Circle() I created: Input are (1) the coordinates in form (x, y) and (2) pressure of touch
circle1 = Circle((100, 200), 2)
circle2 = Circle((500,300), 10)
circle3 = Circle((-660,-250), 8)
circle4 = Circle((0,230), 6)
circle5 = Circle((300,0), 9)

screen.exitonclick()
