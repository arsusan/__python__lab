#number guessing game
import random
def numbers(user_input, target, count):
 
    if user_input == target:
        print("You got the number.")
    elif user_input > target:
        print("number is smaller.")
        count = count - 1
    elif user_input < target:
        print("number is greater.")
        count = count - 1


for i in range(3):
    user_input = int(input("Guess a number: "))

    target_number = random.randrange(1,20)

    numbers(user_input, target_number, 0)


print("The number is ", target_number, " better luck next time.")