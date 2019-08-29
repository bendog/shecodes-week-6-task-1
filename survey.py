from question import Question
from section import Section
from keep_answers import answer_dictionary

class Survey():
# define survey parameters : title, description, sections
    def __init__(self,title,description,qualify_questions,survey_sections):
        self.title = title
        self.description = description
        self.qualify_questions= qualify_questions
        self.survey_sections=[]


    def ask_if_wants_to_continue(self):
        while True:
            user_answer = input('Do you want to continue with survey?Enter yes/no to continue. ').lower()
            # Check if answer
            if user_answer== 'yes':
                continue
            elif user_answer=='no':
                print ('Appreciate you time.\nExiting.')
                break
            else: 
                print ('Invalid input.\nExiting.')
                break 

    # check if user answer for qualify question is yes then make a list of questions and compare with section qualify question list.
    # if they match run the section         

        
    def ask_qualify_question(self):
        isqualify=[]
        for question in self.qualify_questions:  
            question.ask_question()  # ask if these two will work when ask_question() and get_user_answer() are methods in Question
            isqualify.append(question.get_user_answer())
        return isqualify    


    def survey_introduction(self):
        print(f'============================ {self.title} ============================\n')
        print(f'{self.description}\n\n')   
        self.ask_if_wants_to_continue()
        for section in self.survey_sections:
            if self.ask_qualify_question() in self.survey_sections.qualifying_question: 
                # has error 
                # ask how can I get the qualify list of section in servey???
                section.run_section()
        
    
    

        

        









    