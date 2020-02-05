# List

# Defining a list
# syntax
    # = []
    #crazy_landlords = []
# list are organised using Index

crazy_landlords = []
print(type(crazy_landlords))

# We can dynamically define a list
# or re-define a list
crazy_landlords = ['Mr Richards', 'Raj', 'Mr. Shirk', 'Zmem', 'Zemmuwn' ]

# Acess obj in a list4
# list are organised using Index
# name_list = [     0       ,       1   ,       2       ,       3]
# to access landlord Raj, we need the index number 1.

crazy_landlords = ['Mr Richards', 'Raj', 'Mr. Shirk', 'Zmem', 'Zemmuwn' ]
print(crazy_landlords[1])

# We can also redefine at a specific index
# Change Zemmuwn to Alice
print('changing index number 4 to alice')
crazy_landlords[4] = 'Alice'
print(crazy_landlords)
crazy_landlords[-1]

 # another way to get length and make index
length_list = len(crazy_landlords)
last_index = length_list - 1
print(crazy_landlords[last_index])

 # Adding a record to the list
 # .append(obj)

crazy_landlords.append('LANA!')
print(crazy_landlords)

#what if need to insert into a specific index
#.insert()

crazy_landlords.insert(2, 'Mr Paiva')
print(crazy_landlords)

# Remove item from list, according to value
# .remove(arg) --> returns the list without value or arg

crazy_landlords.remove('Zmem')
print(crazy_landlords)#

#remove using index - or last entry
#.pop()

crazy_landlords.pop()   #remove entry on last entry
print(crazy_landlords)

#removing at specific index

crazy_landlords.pop(1) #removing Raj from the list

# # we can have mixed data list

hybrid_list = ['JSON', 'Jason', 13, 53, [1, 2]]
print(hybrid_list)

## Tuple
# immutable list - cant changed
my_tuple = (2, 'hello', 22, 'more values')
print(my_tuple)
print(my_tuple[1])
print(my_tuple[1])

#my_tuple[0] = 10 ---> this breaks as we trying to change the tupe
#
print(my_tuple[1][0])

#Range Slicing
print(crazy_landlords[0:1]) #0 to 1, not inclusive of 1
print(crazy_landlords[1:2]) #1 to 2, not inclusive of 2

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Jumping/slicing
# syntax[N:O:M]
# N is where it starts (index)
# M is every record it jumps (length not INDEX)
# O is where it sends (index)
print(example_list[0:8:2])
print(example_list[2:5:1])

# we need more info for our language

# crazy_landlords = ['Mr Richards', 0783435345, 'Alice', 4754645654 'James',]

# We need to add more data
