class Quizbrain:

    def __init__(self, qlist):
        
        self.qlist = qlist
        self.question_num = 0
        self.score = 0 

    def next_question(self):

        current_question = self.qlist[self.question_num]
        self.question_num += 1
        user_input = input(f"Q.{self.question_num}: {current_question.text} (True/False)? ").lower()
        self.check_answer(user_input, current_question.answer)
        
    def still_questions(self):

        if self.question_num < len(self.qlist):
            return True
        else:
            print("You've reached the end!")
            return False 

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"You're score is {self.score} / {self.question_num}")
            print()
        else:
            print("You got it wrong!")
            print(f"You're score is {self.score} / {self.question_num}")
            print()
        