# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list # como o que está sendo passado é um objeto do tipo Question, então tenho acesso ao atributo .text
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # Poderia ser feito assim:
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        # user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)")
        # self.question_number += 1
        
        # Poderia fazer assim
        current_question = self.question_list[self.question_number] # List[index]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer) # porque o que esta sendo passado é um objeto do tipo Question, então tenho .answer

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {current_question}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")