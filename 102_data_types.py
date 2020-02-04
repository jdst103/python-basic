# strings
# these are list of characters put together, in a list
#defined by '' or " "

my_string = "amazing grilled fish"
print(my_string)
print(type(my_string))

#concatenation
# joining of two strings
first_name = 'Boris'
last_name = 'May'

#polymorph
print(first_name, last_name)

full_name = first_name + ' ' + last_name
print(full_name)

#polymorph
print(first_name, last_name, 'more strings')

#interpolation
#inject a string into another string
#place a f behind the string and use {} inside the string to interpolate the variable/python
name = 'Lana'
welcome_message = "welcome to the DANNNGGERRRZOOONE!"
print(f"{name*10}, welcome to the DANNNGGERRRZOOONE!")

#ORA

intepolated_welcome_message = f"{name*10}, welcome to the DANNNGGERRRZOOONE!"
print(intepolated_welcome_message)


#special methods for string
my_string = " hELeLLO this is an Amazing string"

# .count()
print(my_string.count('i'))
print(my_string.count(' '))

#.strip() removes trailing white spaces
print(my_string)
print(my_string.strip())

#len() - function not a method!!!
print(len(my_string))
print(len(my_string.strip()))

#.capitalized()
print(my_string.strip().capitalize())

# a method to make everything caps
print(my_string.upper())
# a method to make everything lower
print(my_string.lower())
# a method to seperate the string into several strings
print(my_string.strip().split())
print(my_string.strip().split(' '))
print(my_string[2])

#.split(arg)  will output list
