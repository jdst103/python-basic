student1 = {
    'name': 'Morty',
    'stream': 'universal quest',
    'grade': '12',
}

student2 = {
    'name': 'Summer',
    'stream': 'Terrestial quest',
    'grade': 20
}
#List of Dictionaries
student_list = [student1, student2]

#print(student_list[1])

#Dictionarires of Dictionaires
students_dict = {
    'student1': student1,
    'student2': student2
}

#Use the list to print the individual names
# --> Morty
# --> Summer

# print(type(student_list))
st1 = (student_list[0])
#print(type(st1))
print(st1['name'])

#broken down for 'Morty' above

st2 = (student_list[1]['name'])
print(st2)


#Use the dictionaires to print the individual names
# --> Morty
# --> Summer

st11 = students_dict['student1']['name']
print(st11)

#broken down for summer bwlow

st22 = students_dict['student2']
print(st22['name'])