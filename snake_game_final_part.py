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
scores.high_score()


#snakefood

khaana = SnakeFood()


#game movements

game_on = True
score = 0
# highscore = 0

while game_on:


    # collision object

    
    my_scr.update()

    time.sleep(0.1)

    # scores= ScoreBoard(score)


    naag.movement()

            
    #game over
    if naag.head.xcor() > 285 or naag.head.xcor() < -285 or naag.head.ycor() > 285 or naag.head.ycor() < -285:
        naag.reset_body()
        scores.reset_score()
        score = 0


    if naag.head.distance(khaana) < 11:
        khaana.new_pos()
        score+=1 
        scores.updating(score)
        naag.inc_len()
        
        


    for each in naag.segments[1:]:

        if naag.head.distance(each)< 10:
                    naag.reset_body()
                    scores.reset_score()







    




        
        
        
        
        


my_scr.exitonclick()
