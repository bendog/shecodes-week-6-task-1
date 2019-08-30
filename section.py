from question import Question


class Section:

    def __init__(self, sec_title, sec_description, question_list, qualifying_question):
        self.sec_title = sec_title
        self.sec_description = sec_description
        self.qualifying_question = qualifying_question
        self.question_list = question_list
        # self.first_question = first_question  # @bendog - i've removed first question as it seems to make less sense

    def ask_qualify_question(self):
        # @bendog - i moved this method here, because it seemed to make sense to keep it as part of the data object it was using
        # isqualify = []
        if self.qualifying_question:
            self.qualifying_question.ask_question()  # ask if these two will work when ask_question() and get_user_answer() are methods in Question
            # isqualify.append(self.qualifying_question.get_user_answer())
        # @bendog - this might not be doing what you want it to be doing
        return self.qualifying_question.user_answer

    # run method for each section

    def run_section(self):
        print(f'============================ {self.sec_title} ============================\n')
        print(f'{self.sec_description}\n')
        for question in self.question_list:
            question.ask_question()
            # question.get_user_answer()  # @bendog - this was already being asked in the ask_question()
            question.print_user_answer()
            # self.user_answers = question.keep_answers()  # @bendog - is this meant to be part of section?

        # for key, value in self.user_answers.items():
        #     print(f'your answer for {key} is {value}')

        # @bendog - since you are storing your answers in the question, you can list over the questions to get answers
        for question in self.question_list:
            print(f'your answer for {question.question_text} is [{question.user_answer}] {question.user_answer_text}')
        print('Print Thank you messgae: Thanks for your time.bala bala bala....')
        # exit()  # how to add exit comand search for this
        pass  # @bendog - using exit() will quit the entire app, you might not want this.
        # a method (or function) will just end when it runs out of code to process
        # ALSO be very mindful of your indentation, most of your problems are probably because the methods weren't indented correctly.
