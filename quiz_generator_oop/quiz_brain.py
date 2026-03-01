

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_q_left ( self ):
        return self.question_number < len(self.question_list) 
    

    def next_question(self):
        correct_ans = self.question_list[self.question_number].answer
        user_input = input(f"Q.{self.question_number+1}.{self.question_list[self.question_number].question}? (true/false) ").title()
        self.question_number += 1
        self.check_ans(user_input, correct_ans )

    def check_ans(self , user_ans  , correct_ans):

        if ( user_ans == correct_ans ):
            print("You are correct!!!")
            self.score +=1

        else:
            print("Incorrect...")

        print(f"The correct answer was {correct_ans}!")
        print(f"Your current score: {self.score}/{self.question_number}")



    def quiz_ended(self):
        print("\nThe quiz has completed yayyy!!")
        print(f"Your final score is : {self.score}/{self.question_number}")