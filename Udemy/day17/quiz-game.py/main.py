from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main():
    question_bank = []

    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        question = Question(question_text, question_answer)
        question_bank.append(question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()
    

if __name__ == "__main__":
    main()