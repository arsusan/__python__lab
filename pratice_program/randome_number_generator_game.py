'''
1. Develop a game where the computer randomly selects a number within a specified range, and the user has to guess the number.
Provide hints if the guessed number is too high or too low.
After user guess correct number display guess attempts and the exact answer too.
Make sure user does not input other than integer, if its other data type show them invalid input.

Hint: Use while loop, generate random number use python random.randint() function
'''

import random, sys

print("\n Welcome to number guessing game. \n \t Here you have to guess a number with a specific range. \n\t You can guess the number 3 time, if you wiil not able to guess the number then you will loose the game.\n")
randome_number = random.randrange(10, 20)
print("You have to choose the number in between 10 and 20.")

count = 3
while count > 0:
    user_input = int(input("Guess the number: "))
    # if user_input is not int:
    #     print("Error!...Enter a integer number.")
    if user_input>= 10 and user_input <= 20:
        if user_input < randome_number:
            print("Number is Higer.")
            count = count - 1
        elif user_input > randome_number:
            print("Number is Lower.")
            count = count - 1
        elif user_input == randome_number:
            print("You got the number.")
            print(f"\n\t\tYou got the number, which is {randome_number}")
            sys.exit()
    else:
        print("Number is out of range.")

print(f"You loose the game, try next time. \n The number is {randome_number}\n")