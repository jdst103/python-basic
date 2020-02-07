import time
# The game Fizz AND Buzz!

def check_3(number):
    return (number % 3 == 0)

def check_5(number):
    return (number % 5 == 0)

def increase_number(number):
    return number + 1

def time_sleep():
    return time.sleep(0.1)

game = 'GO'
while game != 'STOP':

    # as a user I should be ask for a number,
    number = input('Insert any number:  ')
    number = int(number)

    # As a player, I should see the game counting up to my number and
    # substituting the Multiples of 3 and 5 with the appropriate values,
    # so that I can play the game with my input
    for number in range(1,10):

        # multiples of 3 and 5 are FizzBuzz
        if check_3(number) and check_5(number):
            print('FizzBuzz!')
            time_sleep()
            # increase_number(number) # Can use this function if using a while loop #

        # multiple of 3 are POP
        elif check_3(number):
            print('POP!')
            #increase_number(number) #
            time_sleep()

        # multiple of 5 are TOC
        elif check_5(number):
            print('TOC!')
            #increase_number(number) #
            time_sleep()

        else:
            print(number)
            #increase_number(number) #
            time_sleep()

    # As a player, I should be able to exit the game using a key word,
    # so that I can stop playing
    game = input("Enter 'STOP' to finish the game, or 'GO' to continue the game\n:")
    game = game.strip().upper()

    if game == 'STOP':
        print('Thank you for playing this game!!')
