import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "Udemy/26-day/us-states-game-start/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

game_is_on = True


def write_state(x, y, state):
    drawer = turtle.Turtle()
    drawer.ht()
    drawer.penup()
    drawer.goto(x, y)
    drawer.write(f"{state}", align="center", font=FONT)


# How to get coordinates of the turtle screen for the game
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("Udemy/26-day/us-states-game-start/50_states.csv")

states = data["state"]

# print(states == "Alabama")

state = data[data.state == "Alabama"]
# print(state)
# print(state.x)

correct_guesses = []
score = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    for state in states:
        if answer_state == state:
            if answer_state not in correct_guesses:
                correct = data[data.state == state]
                x = int(correct.x)
                y = int(correct.y)
                correct_guesses.append(answer_state)
                score+=1
                write_state(x=x, y=y, state=answer_state)
                game_is_on = True

        if len(correct_guesses) == 50:
            write_state(x=-10, y=0, state="You win!")
            game_is_on = False

states_to_learn = []
for state in states:
    if state not in correct_guesses:
        states_to_learn.append(state)

# Using list comprehension will be like this (putting 4 lines in one)
# states_to_learn = [state for state in states if state not in correct_guesses]

# print(states_to_learn)

states_to_learn_dict = {
    "states": states_to_learn
}

# print(states_to_learn_dict)


# Creating a new file containing the missing states
new_table = pandas.DataFrame(states_to_learn_dict)
new_table.to_csv("Udemy/26-day/us-states-game-start/states_to_learn.csv")


