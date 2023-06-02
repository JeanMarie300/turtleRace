from turtle import Turtle, Screen
from random import *

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which title will win the race? Enter a color: ")
colors = ["red", "orange", "yellow","green","blue","purple"]
all_turtles = []
is_race_on = False
yval = 100
for i in range (0, len(colors)) :
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x= -230, y=yval)
    yval -= 40
    all_turtles.append(turtle)

if user_bet :
    is_race_on = True
    while is_race_on :
        for turtle in all_turtles :
            if turtle.xcor() > 230 :
                is_race_on = False
                winning_clor = turtle.pencolor()
                if winning_clor == user_bet :
                    print("Congratulation you have won")
                else:
                    print(f"You lost , the turtle {winning_clor} won")
            else:
                turtle.forward(randint(0,10))

screen.exitonclick()
