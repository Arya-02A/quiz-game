class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.q_num < len(self.q_list)
    
    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {current_q.text}. (True/False) :")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is: {self.score} / {self.q_num}")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")