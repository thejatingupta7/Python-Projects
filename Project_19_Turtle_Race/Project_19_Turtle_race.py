from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(height=700, width=600)     # x axis = 500; y axis = 400
user_guess = screen.textinput(title="Make a choice", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
y_range = [300, 200, 100, 0, -100, -200, -300]
all_turtles = []

for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.pu()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_range[i])
    all_turtles.append(tim)

if user_guess:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 280:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_guess:
                print(f"You won! The {winner} turtle is the winner.")
            else:
                print(f"You Lose! The {winner} turtle is the winner.")
        movement = random.randint(1, 10)
        t.fd(movement)

screen.exitonclick()
