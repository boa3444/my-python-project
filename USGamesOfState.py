from turtle import Turtle, Screen
import pandas as pd
from USstatesClass import StateNameCreator
from USScoreboard import Score



#map of US
background = Screen()
background.title("United States Map")
USmap= "blank_states_img.gif"
background.addshape(USmap)
background.setup(900, 600)

formap= Turtle()
formap.shape(USmap)


#scoreboard
scoreboard= Score()

#
states_data = pd.read_csv("50_states.csv")



correct_guesses = 0
already_guessed= []

while correct_guesses < 50:
    guess = background.textinput("Guess The State","Type a state name down here:").title().strip()

    for state in states_data.loc[:,'state']:

        if guess == state and guess not in already_guessed:
                statename = StateNameCreator(state)
                row = states_data[states_data.state == guess]
                set_x = int(row.iloc[0,1])
                set_y = int(row.iloc[0,2])
                statename.teleport_name(set_x, set_y)
                already_guessed.append(state)
                correct_guesses += 1
                scoreboard.update_score(correct_guesses)

        else:
            continue




background.exitonclick()