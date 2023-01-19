from question_model_p import Question
from data_p import question_data
from quiz_brain_p import QuizBrain
from ui_p import QuizInterface

count = 0
count_q = 0

question_bank = []


for question in question_data:

    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    count_q += 1


quiz = QuizBrain(question_bank)

ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
