# Control flow
# if statements
# Control where the code will execute. Depending on the assertions.
# An assertion/condition is something that returns True or False

# notes:
# block of code - refers to a consecutive lines of code, that are indented and
#will run together. Block exist inside if statments and while loops and other functions.
# in simple words: its a specific piece of code that will run in a specific time.


# # # Syntax

# if <condtion>:
#      # block of code
#   elif <conditionL:
#   # block of code
#else:
#   # block of code

#weather = 'rainy and stormy'
#if weather == 'rainy':
 #   print('take umbrella!')
  #  print("I'm still in the block of code aswell")
#elif weather == 'stormy':
 #   print('take rain coat')
#elif 'stormy' in weather and 'rainy' in weather:
 #   print('stay ay home')
#else:
#    print('Take sunglasses')###


weather = 'rainy and stormy'
if 'stormy' in weather and 'rainy' in weather:
    print('stay ay home')

elif weather == 'rainy':
    print('take umbrella!')

elif weather == 'stormy':
    print('take rain coat')
else:
    print('Take sunglasses')

#print("I'm outside and always run :D")

