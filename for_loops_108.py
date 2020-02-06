import time

# for loops
# iterations!

# syntax

# for <placeholders> in <iterable>:
    #block of code
    # indented lines are part of this block



cars = ['skoda felecia fun', 'Mustang Boss 429', 'Fiat 500', 'Jaguar 420g', 'Aston Martin Vanquish']

#for x in cars:
#    print(x)
 #   time.sleep(1)
  #  print('still in the block')

#for x in cars:
 #   print(x)
  #  time.sleep(1)

#for car in cars:
#    print(car)
 #   time.sleep(1)

#iterating over a dictionary
student1 = {
    'name': 'Arya Stark',
    'stream': 'Many faces',
    'grade': '10'

}
#gives key
#for x in student1:
#    print(x)

#print(student1['name'])

#for key in student1:
 #   print(key)

#for key in student1:
#    print(key) # this is each individual key of the dictionnary
 #   print(student1)#  this is the dictionary
  #  print(student1[key]) # we can use the dictionary + keys to get the values

# iterate over the student1
# i want the output to be
    # -> 'name is Arya Stark'
    # -> 'stream is Many Faces'

for key in student1:
    print(key.capitalize(), 'is ' + student1[key])

for key in student1:
    print(f"{key} is {student1[key]}")

    # -> 'stream is Many Faces'
