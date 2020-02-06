# Functions
# Functions have one job
# Functions are like machines,
#it needs to be turn on
#They can take in inputs (optionally), do some work (block of code), and have  outputs
# It makes you code more readable, maintainable and testable.

# functions need to be defined and call that function

#Best Practices
# --> Functions do one small task. --> this makes them testable
# generally dont print inside a function. you return

# Dry
# Dont
# Repeat
# Yourself

#Run a block of code when called.
#
#Syntax

#def <name>(arg,arg2):
#   block of code
#   block of code
    #return something (optional)

# function no arguments
def say_hello():
    return 'hello'

#print(say_hello()) # calling a function

#function with arguments
def full_name(f_name, l_name):  #taking in two arguments
    return f_name +' ' + l_name

#print(full_name('Bernie', 'Sanders'))

def welcome_message(f_name, l_name):
    full_name_str = full_name(f_name, l_name)
    welcome_str = say_hello()
    return welcome_str + ' ' + full_name_str

print(welcome_message('filipe', 'paiva'))


def adding(num1, num2):
    return num1 + num2

print(adding(300,300))