def respect(student_question, student_question_list):
    student_question_list = student_question.split()
    return student_question_list[0] != 'Sensei'

def block(student_question):
    return 'block' in student_question

def ask_question(student_question):
    return  '?' in student_question



