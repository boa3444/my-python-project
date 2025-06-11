from turtle import Turtle



class ScoreBoard():

    def __init__(self):
        self.scoreboard= Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0,277)
        self.scoreboard.color("white")
        self.updating(0)

    def updating(self, update_score):
        scoreboard =self.scoreboard
        scoreboard.clear()
        scoreboard.write(arg=f"SCORE: {update_score}",  align="center", font = ('Ariel', 15, 'normal'))

    


    def Gameover():
            gameover = Turtle()
            gameover.penup()
            gameover.color("yellow")

            gameover.write( arg= "GAME OVER",align = 'center' ,font= ('Times New Roman', 50, 'normal'))




