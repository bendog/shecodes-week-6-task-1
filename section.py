from question import Question


class Section:
    
    def __init__ (self,sec_title,sec_description,question_list,first_question=None,qualifying_question=None,user_answers={}):
        
        self.sec_title = sec_title
        self.sec_description = sec_description
        self.qualifying_question = qualifying_question
        self.question_list = question_list
        self.first_question = first_question




# run method for each section

def run_section(self):
        print(f'============================ {self.sec_title} ============================\n')
        print(f'{self.sec_description}\n')
        for question in self.question_list:
            question.ask_question()
            question.get_user_answer()
            question.print_user_answer()
            self.user_answers = question.keep_answers()
        for key, value in self.user_answers:
            print(f'your answer for {key} is {value}')
        print ('Print Thank you messgae: Thanks for your time.bala bala bala....')
        exit # how to add exit comand search for this          



