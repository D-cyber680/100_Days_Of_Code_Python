import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
text = turtle.Turtle()
text.penup()
text.ht()
# Cambiar fondo
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_cor(x, y):
# print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)
us_data = pandas.read_csv("50_states.csv")
us_states_list = us_data.state.to_list()
score = 0


def get_xcor_state(answer_state):
    return int(us_data[us_data.state == answer_state].x)


def get_ycor_state(answer_state):
    return int(us_data[us_data.state == answer_state].y)


while len(us_states_list) > 0:
    answer_state = screen.textinput(title = f" {score}/50 Guess the state", prompt="What's another's state name?").title()

    if answer_state == "Exit":
        break
    if answer_state in us_states_list:
        score += 1
        x = get_xcor_state(answer_state)
        y = get_ycor_state(answer_state)
        text.goto(x, y)
        text.write(answer_state, align="left", font=("Arial", 8, "normal"))
        us_states_list.remove(answer_state)

    missing_states_dict = {
        "States": us_states_list
    }

    data_states = pandas.DataFrame(missing_states_dict)
    data_states.to_csv("states_to_learn.csv")

turtle.mainloop()
