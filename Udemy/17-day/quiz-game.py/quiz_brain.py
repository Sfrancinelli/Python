from question_model import Question
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {q_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")




            

