"""this where magic happens"""
from question_model import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []
for text,answer in question_data:
    question_bank.append(Question(text,answer))

quiz = quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
