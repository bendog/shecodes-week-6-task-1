from keep_answers import answer_dictionary

class Question:
    def __init__(self,q_number,question_text,question_answers,valid_answers=None,next_question=None):
        self.q_number= q_number
        self.question_text = question_text
        self.question_answers= question_answers
        self.next_question = next_question
        self.valid_answers=[]

# ask question from user
def ask_question(self):
        print(f'{self.q_number} {self.question_text}\n')
        for answer_code,answer_text in self.question_answers.items():
            print(f'{answer_code} {answer_text}')
        self.get_user_answer()
        self.print_user_answer()    
        print('\n')


# show user answer after each question : 
def get_user_answer(self):
        #ToDo: add validator for user answer /check if code is in the valid_answers
        user_answer = input('Your answer is: ')
        return user_answer
        
def print_user_answer(self):        
        print (f'Your answer for question {self.q_number} {self.question_text} is {user_answer}')
                    

#keep a dictionary of question text and user answers per question : ASk Ben/Hayley should I put this method in section or question class? 
def keep_answers(self):
    self.answer_dict = answer_dictionary() 
    self.answer_dict.key = self.question_text
    self.answer_dict.value = input()
    self.answer_dict.add(self.answer_dict.key, self.answer_dict.value)
    return self.answer_dict   