import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_done = False

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
not_guessed = [str("The ones you missed:")]

while len(guessed_states) < 50 and game_is_done == False:
    answer_state = screen.textinput(title=f"Guessed:{len(guessed_states)}/50 States", prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Done":
        game_is_done = True

screen.exitonclick()

for un_guessed in all_states:
    if un_guessed not in guessed_states:
        not_guessed.append(un_guessed)

data_csv = pandas.DataFrame(not_guessed)
data_csv.to_csv("Missed.csv")

