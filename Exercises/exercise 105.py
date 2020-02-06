#exercise 1
age = 19
driver_license = True

#you can vote and drive
if age >= 18 and driver_license == True:
    print('You can vote and drive')

# you can vote vote
elif age >= 18:
    print('You can vote')

#you can drive
elif driver_license == True:
    print('You can drive')

# you cant legally drink but your mates have your back (bigger 16)
elif 16 <= age <18:
    print('Sorry mate come back when you older')
else:
    print('Your too young, go back to school!')