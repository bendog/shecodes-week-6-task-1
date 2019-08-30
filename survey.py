from question import Question
from section import Section
from keep_answers import answer_dictionary


class Survey:
    # define survey parameters : title, description, sections
    def __init__(self, title, description, qualify_questions, survey_sections):
        self.title = title
        self.description = description
        self.qualify_questions = qualify_questions
        # self.survey_sections = []
        self.survey_sections = survey_sections  # @bendog - survey sections were never assigned, this might have caused some troubles

    def ask_if_wants_to_continue(self):
        while True:
            user_answer = input('Do you want to continue with survey?Enter yes/no to continue. ').lower()
            # Check if answer
            if user_answer == 'yes':
                return True  # @bendog return True to end the loop
            elif user_answer == 'no':
                print('Appreciate you time.\nExiting.')
                return False  # @bendog return False to end the loop in the negative
            else:
                print('Invalid input.')

                # check if user answer for qualify question is yes then make a list of questions and compare with section qualify question list.

    def survey_introduction(self):
        print(f'============================ {self.title} ============================\n')
        print(f'{self.description}\n\n')
        if self.ask_if_wants_to_continue():  # @bendog this is now an if statement to check if the user wants to continue
            for section in self.survey_sections:
                if section.ask_qualify_question():
                    # has error
                    # ask how can I get the qualify list of section in servey???
                    # @bendog - i've moved the ask_qualifying_question to the section, i did this because the qualifying question is part of the section.
                    # also the reason you might have been having trouble is that there is only one qualifying_question, and so it is not in a list.
                    # the code here was expecting it to be a list, so it wasn't working.
                    section.run_section()
