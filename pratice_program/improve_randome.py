import random
import sys

def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print("\tYou have to guess a number within a specified range.")
    print("\tYou can guess the number 3 times. If you are unable to guess correctly, you will lose the game.\n")

def get_random_number(start, end):
    return random.randint(start, end)

def get_user_input():
    while True:
        try:
            user_input = int(input("Guess the number: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter an integer.")

def check_guess(user_input, random_number):
    if user_input < random_number:
        print("The number is higher.")
        return False
    elif user_input > random_number:
        print("The number is lower.")
        return False
    else:
        print("You guessed the number correctly!")
        print(f"\n\tThe correct number is {random_number}")
        return True

def main():
    # it will print the welcome message
    welcome_message()
    
    start, end = 10, 20 #starting and ending index
    random_number = get_random_number(start, end)
    print(f"You have to guess a number between {start} and {end}.")
    
    attempts = 3 #number of attnemps 
    while attempts > 0:
        user_input = get_user_input() #get user input
        
        if user_input < start or user_input > end:
            print(f"Number is out of range! Please guess a number between {start} and {end}.")
            continue
        
        if check_guess(user_input, random_number):
            print(f"It took you {3 - attempts + 1} attempts to guess the correct number.")
            sys.exit()
        
        attempts -= 1
    
    print(f"You lose the game. Try next time.\nThe correct number was {random_number}.\n")

if __name__ == "__main__":
    main()
