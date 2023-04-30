from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = list()
for dictionary in question_data:
    question_bank.append(Question(dictionary['text'], dictionary['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz, your final score is {quiz.score}/{quiz.question_number}")