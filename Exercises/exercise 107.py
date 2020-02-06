import time
# The game Fizz AND Buzz!

game = 'GO'

while game != 'STOP':

    # as a user I should be ask for a number,
    number = input('Insert any number!')
    number = int(number)

    # As a player, I should see the game counting up to my number and
    # substituting the multiples of 3 and 5 with the appropriate values,
    # so that I can play the game with my input
    for number in range(1,10):

        # multiples of 3 and 5 are FizzBuzz
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz!')
            number = number + 1
            time.sleep(0.1)

        # multiple of 3 are POP
        elif number % 3 == 0:
            print('POP!')
            number = number + 1
            time.sleep(0.1)

        # multiple of 5 are TOC
        elif number % 5 == 0:
            print('TOC!')
            number = number + 1
            time.sleep(0.1)

        else:
            print(number)
            number = number + 1
            time.sleep(0.1)

    # As a player, I should be able to exit the game using a key word,
    # so that I can stop playing
    game = input("Enter 'STOP' to finish the game, or 'GO' to continue the game")
    game = game.strip().upper()





