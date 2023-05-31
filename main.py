from question_bank import question_bank
from Question import Question
from quizbrain import Quizbrain

questions = []

for question in question_bank:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    questions.append(new_question)


quiz = Quizbrain(questions)

while quiz.still_questions():
    quiz.next_question()