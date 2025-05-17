#decorations 
print('''

████████▄   ███    █▄   ▄█   ▄████████            ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ 
███    ███  ███    ███ ███  ██▀     ▄██             ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ 
███    ███  ███    ███ ███▌       ▄███▀             ███    █▀    ███    ███ ███   ███   ███   ███    █▀  
███    ███  ███    ███ ███▌     ▄███▀              ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄     
███    ███  ███    ███ ███▌   ▄███▀               ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀     
███    ███  ███    ███ ███  ▄███▀                   ███    ███   ███    ███ ███   ███   ███   ███    █▄  
███  ▀ ███  ███    ███ ███  ███▄     ▄█▄             ███    ███   ███    ███ ███   ███   ███   ███    ███ 
 ▀██████▀▄█ ████████▀  █▀    ▀████████▀             ████████▀    ███    █▀   ▀█   ███   █▀    ██████████ 
                                                                                                         

''')
#logic of quiz
from data import question_data
numbering = list(range(0,13))

class QuestionAnswer:
    def __init__ (self, question , answer):
        self.question = question
        self.answer = answer
    
    def perform_action(self):
        
                print(f"Your question is : {self.question}")




class QAChecker:
    def __final__(self):
                score = 0
        
            
                for item in question_data:
                    
                        question = item['text']
                        answer = item['answer']
                        # print(q_a.question)
                        
                        question_answer = QuestionAnswer(question, answer)
                        
                        question_answer.perform_action()

                        user_input = input("Type True/False : ").title()
                        if user_input == answer:
                            score += 1
                            print("You are correct!")
                            print(f"Your current score: {score}")
                        elif user_input != answer:
                            print("You are incorrect!")
                            print(f"Your total score: {score}")
                            break
                        else:

                            print("Make sure your input is correct.")
                            break
                        


final_checker = QAChecker()
final_checker.__final__()



