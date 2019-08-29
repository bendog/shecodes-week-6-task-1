from question import Question
from section import Section
from keep_answers import answer_dictionary
from survey import Survey

def main():
# create objects of questions and sections for servey    
    qualify1=Question('1','Question 1 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    qualify2=Question('2','Question 2 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    qualify3=Question('3','Question 3 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q4=Question('1','Question1 Section1 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q5=Question('2','Question2 Section1 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q6=Question('3','Question3 Section1 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q7=Question('1','Question1 Section2 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q8=Question('2','Question2 Section2 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q9=Question('3','Question3 Section3 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q10=Question('1','Question1 Section3 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q11=Question('2','Question2 Section3 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})
    q12=Question('3','Question3 Section3 12 text? ',{'[A]': 'AnswerA' ,'[B]': 'AnswerB','[C]':'AnswerC'})

    sectionA=Section('SectionA Title' , 'Here is some info about what we covered in sectionA',[q4,q5,q6],qualify1,q4)
    sectionB=Section('SectionB Title' , 'Here is some info about what we covered in sectionB',[q7,q8,q9],qualify2,q7)
    sectionC=Section('SectionC Title' , 'Here is some info about what we covered in sectionC',[q10,q11,q12],qualify3,q10)
    qualifyquestion= [qualify1,qualify2,qualify3]

    my_survey = Survey ( 'SheCodes Survey','This is a placeholder for Description on Survey',qualifyquestion,[sectionA , sectionB, sectionC])
    my_survey.survey_introduction()
# start 

if __name__ == "__main__":
    main()      
