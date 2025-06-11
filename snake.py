from turtle import Turtle, Screen


my_scr = Screen()


coordinates = [(0,0), (-20, 0), (-40,0)]



class Snake():
    def __init__(self):
        self.segments = []
       
    
        
    def body(self, coordinate):
            
       
            segment= Turtle("square")
            segment.color("white")
            segment.shapesize(1)
            segment.speed("fastest")
            self.segments.append(segment)
            segment.penup()
            segment.goto(coordinate)
            # # 

            # for each in self.segments:
            #     if naag.head.distance(each.pos())< 10:
            #          game_ob = False
            #          break
    
    def create_body(self):
        for coordinate in coordinates:
            self.body(coordinate)
                


        self.head = self.segments[0]
        # return self.head

    def inc_len(self):
        
        self.body(self.segments[-1].pos())
        # self.segments.append(new_segment)
    
            
         
    def movement(self):
        # head= self.head
        
        def turn_right():
            self.head.setheading(0)

        def turn_left():
            self.head.setheading(180)

        def turn_up():
            self.head.setheading(90)

        def turn_down():
            self.head.setheading(270)
        
            
        my_scr.listen()
            

        my_scr.onkey(turn_right, "Right")
        my_scr.onkey(turn_left, "Left")
        my_scr.onkey(turn_up, "Up")
        my_scr.onkey(turn_down, "Down")

            
            
                
                

        for i in range(len(self.segments) -1 ,0, -1):
                    
                    take_the_front = self.segments[i-1].pos()
                    self.segments[i].goto(take_the_front)

        self.head.fd(20)


