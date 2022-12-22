class Question:

    def __str__(self):
        return "This class stablishes the parameters for the creation of questions for the game."


    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer