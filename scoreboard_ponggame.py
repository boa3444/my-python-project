from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(position)


sb1= Scoreboard((-235, 270))
sb2= Scoreboard((235,270))

sb1.write(arg= f"SCORE: 0",align= 'center', font= ("Algerian", 18, "normal"))

sb2.write(arg= f"SCORE: 0",align= 'center' ,font= ("Algerian", 18, "normal"))

        

class Update:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0

    def update_score1(self):
        sb1.clear()
        self.score1 += 1
        sb1.write(arg=f"SCORE: {self.score1}", align='center', font=("Algerian", 18, "normal"))

    def update_score2(self):
        sb2.clear()
        self.score2 += 1
        sb2.write(arg=f"SCORE: {self.score2}", align='center', font=("Algerian", 18, "normal"))

    

    def Gameover(self):
        if self.score1 ==10 or self.score2==10:

            gameover = Turtle()
            gameover.penup()
            gameover.color("yellow")
            gameover.hideturtle()
            if self.score1 < self.score2:
                gameover.write( arg= f"GAME OVER\n   Right Won",align = 'center' ,font= ('Times New Roman', 30, 'normal'))
            else:
                gameover.write( arg= f"GAME OVER\n   Left Won",align = 'center' ,font= ('Times New Roman', 30, 'normal'))
            
            return True
        
        return False
