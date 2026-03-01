from question_class import QuestionClass
from quiz_questions import questions_list
from quiz_brain import QuizBrain

question_bank =[]

for ele in questions_list:

    new_q = QuestionClass(ele['text'] , ele['ans'])
    question_bank.append(new_q)


q_brain = QuizBrain(question_bank)


while q_brain.still_q_left():
    q_brain.next_question()

q_brain.quiz_ended()