## Dictionaries

# We need to know ehre our crazy landlords live! we need more information!

# Introducing... Dictionaries

# Dictionaries are organised using key value pairs
# Like a real dictionary :)
# you want to look up the word 'omipresent', you dont start
#reading the dictionary from 'A' all the way to 'o'.

# Syntax
# my_dictionary = {
# Create one dictionary
#   'key': 'value', 'other_key': 'other_value'}
my_crazy_x_landlord = {'name': 'Filipe', 'phone': '07842751157'}


#Create one key value pair
my_crazy_x_landlord['address'] = 'Lisboa, Portugal'

# Read all data of dictionary
print(my_crazy_x_landlord)

# Read one entry in a dictionary (read the value of one key)
print(my_crazy_x_landlord['phone'])

#Update the value in a key
(my_crazy_x_landlord['phone']) = '+351 232093030'
print(my_crazy_x_landlord)


# Destroy one key value pair
my_crazy_x_landlord.pop('address')
print(my_crazy_x_landlord)

#Getting all the keys out

key = my_crazy_x_landlord.keys()
print(key)

# getting all the values out

value = my_crazy_x_landlord.values()
print(value)