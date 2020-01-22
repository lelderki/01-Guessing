import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 10  

while not quit: 
    random_number = random.randint(1,range)
    number = input("Please guess a number between 1 and {}: ".format(range))
    number = int(number)
    count = 1
    while number != random_number:
            print("Sorry, you didn't get it right. Try again!")
            if number > random_number:
                print("Too high! Guess again!")
            elif number < random_number:
                print("Too low! Guess again!")
            number = input("Please guess a number between 1 and {}: ".format(range))
            number = int(number)
            count = count + 1
    print("Good job!")
    print("Nice! You guessed it in {} tries!".format(count))
    play_again = input("\nWould you like to play again (yes or no)?")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True