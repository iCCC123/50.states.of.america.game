import turtle
import pandas

screen = turtle.Screen()
screen.screensize(8000, 8000)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()
guesses = []

while len(guesses) < 50:
	answer_state = screen.textinput(title = f"{len(guesses)}/50 guessed states",
									prompt = "What's another state's name?").title()
	print(answer_state)

	if answer_state == "Exit":
		missing_states = []
		for x in state_list:
			if x not in guesses:
				missing_states.append(x)
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if answer_state in state_list:
		guesses.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = states[states.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)


