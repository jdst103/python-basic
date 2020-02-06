def respect(student_question, student_question_list):
    student_question_list = student_question.split()
    return student_question_list[0] != 'Sensei'

def block(student_question):
    return 'block' in student_question

def ask_question(student_question):
    return  '?' in student_question



peace = 'stress'
while peace != 'Sensei, I am at peace':

    student_question = input('\nYes, Mr Miyaji knows the anwser to every question, what is your question?')
    student_question_list = student_question.split()

    if respect(student_question,student_question_list):
        print('You are smart, but not wise - address me as Sensei please')

    elif block(student_question):
        print('Remember, best block, not to be there..')

    elif ask_question(student_question):
        print('questions are wise, but for now. Wax on, and Wax off!')
    else:
        print('do not lose focus. Wax on. Wax off.')

    peace = input("\nif you want to stop playing, \ntype in 'Sensei, I am at peace'.\nTo continue playing, press enter")
