#numerical data types
#ints, long, float, complex
## these are numerical types which can be use numerical operators

##complex and built with imagenary numbers.
# an example would be if you need to track 2 seperate curriencies

#longs are just integers of unlimited size

# int and float
# int stands for integer and they are whole numbers
# floats are numbers with decimals places

#ints
my_int = 10
print(my_int)
print(type(my_int))

#floats
my_float = 10.0
print(my_float)
print(type(my_float))

#operators - add, subtract, divide, multiply and modulus
num1 = 12
num2 = 21
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

#modulus returns the reminder
print(10%3) ## -- v 3*3 = 9, so 1 is the reminder

print(20//3) ##removes decimal

#Comparison operators --> boolen value
## == - equating things on both sides
## < / > - Bigger and smaller
## <= - Smaller than or equal
## >= - Bigger than or equals
## != not equating things on both sides
## is - equates if something is something
## is not - equates if something is not something



my_variables = 10
my_variables2 = 13


print(my_variables == my_variables2)
print(my_variables == 10)
print(my_variables >= my_variables2)

print(my_variables2 is 13)

# Booleans
# True or False
# Binary True or False
print(type(True))


#None
print(None)
print(type(None))

print(0 == None)

#Operators, logical & logical or

a_var = True
b_var = False
#Logical and & requires both sides to be true to result in true syntax
#syntax - both sides needs to be true
# (assertion a & assertion b) --> boolean
print(a_var & True)
print(a_var & False)

#Logical or, only one side needs to be true to return true:
print(' this will be true>>>>')
print(True or False)
james = 'sitting'
print(james == 'sitting' or 10 >300000)
print(james == 'sitting' or False)

#list
my_list = ('blue', 'red', 'yellow', 'green')

#dictionary
my_dictionary = {"Jason": "red", "Hamza": "blue", "Abdi": "yellow"}
