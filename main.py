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

circle1 = Circle((100, 200), 2)
circle2 = Circle((0,0), 10)

screen.exitonclick()
