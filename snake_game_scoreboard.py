from turtle import Turtle



class ScoreBoard():

    def __init__(self):
        self.scoreboard= Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-230,277)
        self.scoreboard.color("white")
        self.updating(0)



    def updating(self, update_score):
        self.update_score = update_score
        self.scoreboard.clear()
        self.scoreboard.write(arg=f"SCORE: {update_score}",  align="left", font = ('Ariel', 15, 'normal'))


    def reset_score(self):
        if self.update_score > self.topscore:
            
            self.updating_high_score(self.update_score)
            with open(r"C:\Users\newon\OneDrive\Documents\snake_game\highscore.txt", mode= 'w') as HSfile:
                HSfile.write(str(self.update_score))

        self.updating(0)

              

    # def Gameover(self):
    #         gameover = Turtle()
    #         gameover.penup()
    #         gameover.color("yellow")
    #         gameover.hideturtle()

    #         gameover.write( arg= "GAME OVER",align = 'center' ,font= ('Times New Roman', 50, 'normal'))


    def high_score(self):
        self.highscore= Turtle()
        self.highscore.hideturtle()
        self.highscore.goto(120,277)
        self.highscore.color("white")
        # self.updating_high_score(0)
        with open(r"C:\Users\newon\OneDrive\Documents\snake_game\highscore.txt") as HSfile:
            self.topscore = int(HSfile.read())
            self.updating_high_score(self.topscore)


    def updating_high_score(self, topscore):
        self.topscore = topscore
        self.highscore.clear()
        self.highscore.write(arg= f"HIGHSCORE: {self.topscore}", align= "left", font = ('Ariel', 15, 'normal'))

