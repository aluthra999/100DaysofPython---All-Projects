import random

import quiz_brain
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question = Question
question_bank = []

for questions in question_data:
    question_text = questions['question']
    question_answer = questions['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.still_have_questions()

while quiz.still_have_questions():
    quiz.next_question()

print("You completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")