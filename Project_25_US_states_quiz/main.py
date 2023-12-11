import turtle
from turtle import Screen, Turtle
import pandas
# Turtle only works with 'gif' files
'''
def get_coordinate_by_click(x, y):          # for getting coordinates on map
    print(x, y)

turtle.onscreenclick(get_coordinate_by_click)
turtle.mainloop()
'''


screen = Screen()
screen.title("U.S. States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_correctly_found = []

while len(states_correctly_found) < 50:
    guessed_state = screen.textinput(title=f"{len(states_correctly_found)}/50 States Correct",
                                     prompt="What's another State's name").title()

    if guessed_state == "Exit":
        missing_states = [i for i in all_states if i not in states_correctly_found]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_remaining.csv")
        break

    if guessed_state in all_states:
        tim = Turtle()
        tim.ht()
        tim.pu()
        state_data = data[data.state == guessed_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(guessed_state, align="center", font=("Arial", 10, "normal"))
        if guessed_state not in states_correctly_found:
            states_correctly_found.append(guessed_state)
