from turtle import  Screen
import time
from snake import Snake
from snake_food import SnakeFood
from snake_game_scoreboard import ScoreBoard

#game background

my_scr = Screen()
my_scr.bgcolor("black")
my_scr.setup(600,600)
my_scr.title("THE SNAKE GAME")
my_scr.tracer(0)




#snake 
naag = Snake()

naag.create_body()

#game scoreboard
scores = ScoreBoard()

#snakefood

khaana = SnakeFood()


#game movements

game_on = True
score = 0

while game_on:


    # collision object

    
    my_scr.update()

    time.sleep(0.2)

    # scores= ScoreBoard(score)


    naag.movement()

    if naag.head.distance(khaana)< 12:
        khaana.new_pos()
        score+=1 
        updates_scores= scores.updating(score)
        naag.inc_len()
        

    if naag.head.xcor() > 285 or naag.head.xcor() < -285 or naag.head.ycor() > 285 or naag.head.ycor() < -285:
        game_on = False
        ScoreBoard.Gameover()



    for each in naag.segments:
        if each == naag.head:
            pass

        elif naag.head.distance(each)< 10:
                    game_on = False
                    ScoreBoard.Gameover()







    




        
        
        
        
        


my_scr.exitonclick()
