"""asks the question"""
#TODO 1.Ask the user for input
class quiz_brain:
    def __init__(self,q_list) -> None:
        self.question_number = 1
        self.question_list = q_list
    def next_question(self):
        self.question_number += 1
        answer = input(f"Q{self.question_number-1}. {self.question_list[self.question_number-1]}" 
                       "(True/False)")
    def still_has_question(self):
        return self.question_number <len(self.question_list)
#TODO 2.Check the answer
#TODO 3.Checking the end of the quiz

