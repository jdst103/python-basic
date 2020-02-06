# Mr miyagi

# mr Miyagi trainee ##projct
# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
# --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
# --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
# --> 'Remeber, best block, not to be there..'
# anything else you say:
# --> 'do not lose focus. Wax on. Wax off.'

# Make it so you keep playing until we say: 'Sensei, I am at peace'
# --> 'Sometimes, what heart know, head forget'



peace = 'stress'
while peace != 'Sensei, I am at peace':

    student_question = input('\nYes, Mr Miyaji knows the anwser to every question, what is your question?')
    student_question_list = student_question.split()

    if student_question_list[0] != 'Sensei':
        print('You are smart, but not wise - address me as Sensei please')
    elif 'block' in student_question:
        print('Remember, best block, not to be there..')
    elif '?' in student_question:
        print('questions are wise, but for now. Wax on, and Wax off!')
    else:
        print('do not lose focus. Wax on. Wax off.')

    peace = input("\nif you want to stop playing, \ntype in 'Sensei, I am at peace'.\nTo continue playing, press enter")
