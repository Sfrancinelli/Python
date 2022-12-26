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
        if answer == current_question.answer:
            self.score += 1
            return True
        else:
            return False 

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True




    # def next_question(self):
    #     answer = True
    #     while answer:
    #         current_question = self.question_list[self.question_number]
    #         answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
    #         if answer == current_question.answer:
    #             self.question_number += 1
    #             answer = True
    #         else:
    #             print("Sorry, thats incorrect!")
    #             answer = False


            

