from arcarde_character import background, Character
from arcade_road import zebra_cross
from arcade_cars import GameCars
import time
from snake_game_scoreboard import ScoreBoard
from WonTheGame import you_won


#zebra cross
background.tracer(False)
zebra_cross()
background.update()

#our character and movements
avatar = Character()


#cars for the blank road
gamecars = GameCars()


#for the gameover
scoreboard= ScoreBoard()


game_on = True
while game_on:


    time.sleep(0.05)
    background.update()
    gamecars.create_cars()
    gamecars.movement()
    background.tracer(False)

    for car in gamecars.game_cars:
        if car.distance(avatar.character) <30:
            game_on= False
            scoreboard.Gameover()
            break

    if avatar.character.ycor() > 295:
        game_on= False
        you_won()
        break

    













background.exitonclick()