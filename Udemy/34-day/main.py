from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

count = 0
count_q = 0

question_bank = []


for _ in range(0, 10):

    question_text = question_data[count]['results'][count_q]['question']
    question_answer = question_data[count]['results'][count_q]['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    count_q += 1


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
