from turtle import *
import pandas as pd

screen = Screen()
pen = Turtle()
pen.color("yellow")
pen.penup()
pen.hideturtle()
image = 'bulacan_map.gif'
screen = Screen()
screen.title("Bulacan Province Game")

def write_state(name, coordinate):
    pen.goto(coordinate)
    pen.write(name, align='center', font=('Arial', 8, 'normal'))

screen.addshape(image)
shape(image)

states_data = pd.read_csv("bulacan_province.csv")
data = states_data.state.tolist()
x = states_data.x.tolist()
y = states_data.y.tolist()

state_dict = {}

for i in range(len(data)):
    state_dict[data[i]] = (x[i], y[i])

screen.addshape(image)
shape(image)

all_state = set(data)
correct_guess = set()

while True:
    #ask for user input
    usr_guess = screen.textinput(f"{len(correct_guess)}/{len(all_state)} ","guess a municipality (Complete Name): ")
    if usr_guess:
        usr_guess = usr_guess.title()

    #check if it is on the list of statename
    if usr_guess in state_dict.keys():

        coordinates = state_dict[usr_guess]
        #go to location, write the statename
        write_state(usr_guess, coordinates)

        #update how many things got right
        correct_guess.add(usr_guess)

    if usr_guess == "Exit":
        break
    if len(all_state) == len(correct_guess):
        print("LETS GO BABYCAKES !!")
        break

#save all the remaining states that are not guessed in a csv file
missing_states = all_state - correct_guess
missing_states_df = pd.DataFrame(list(missing_states), columns=['state'])
missing_states_df.to_csv("missing_states.csv", index=False)

screen.exitonclick()





