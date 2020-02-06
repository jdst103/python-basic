# Make a weather/clothing game ## project
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'
# Make it so you keep playing until we say: 'No more Magic'

# weather = input('Whats the weather like? I can give you advice. :)')

#making my program 'on' intially as default
power = 'ON'

# my game works when my code does not equal the phrase to cancel it.
while power != 'No more Magic':

    # asking user what the weather is like
    weather = input('Whats the weather like? I can give you advice. :)')

    #my control flow
    if weather == 'sunny':
        print('take your shorts!')
    elif weather == 'rainy':
        print('Take your umbrella')
    elif 'rainy' and 'stormy' in weather:
        print('stay home')
    else:
        print("sorry, i didn't quite catch that")

    #inside my while loop, asking if i want to enter my code to cancel this
    power = input("if you want to end the program, enter 'No more Magic',\n if not press enter!")


