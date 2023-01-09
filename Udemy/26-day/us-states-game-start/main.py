import turtle
import pandas

FONT = ("Courier", 20, "normal")

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

print(states == "Alabama")

state = data[data.state == "Alabama"]
print(state)
print(state.x)

correct_guesses = []
score = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name?")
    answer_state = answer_state.title()
    for state in states:
        if answer_state == state:
            correct = data[data.state == state]
            x = correct.x
            y = correct.y
            correct_guesses.append(answer_state)
            score+=1
            write_state(x=x, y=y, state=answer_state)
        else:
            game_is_on = False


turtle.mainloop()

