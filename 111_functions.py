# Functions
# Functions have one job
# Functions are like machines,
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

print(say_hello())