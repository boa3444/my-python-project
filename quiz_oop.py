import json

#TODO: make this oop suitable
with open("/home/divyanshee/Documents/python_practice/quiz_questions.json" , 'r') as file:
    questions_dict = json.load(file)

class quiz_generator:

    def __init__(self):
        self.total_q_asked = 1
        self.got_correct = 0

    
    def ask_questions(self, no_of_q):
            
            for question in questions_dict:
                if self.total_q_asked > no_of_q:
                    break
                user_answer = input(f"{self.total_q_asked}. {question}: ").lower()

                if user_answer == questions_dict[question]:
                    self.got_correct += 1

                print(f"Your score: {self.got_correct}/{self.total_q_asked}")



                self.total_q_asked += 1


quiz1= quiz_generator()

quiz1.ask_questions(6)