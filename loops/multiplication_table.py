'''
Q1. Write a program to print multiplication table of a given number(accept number from user)
eg. if user input 3
3 x 1 = 3
3 x 2 = 6 and so on 
'''

user_number = int(input("Enter number to generate multiplicaiton table."))

for i in range(1,11):
    print(f"{user_number} * {i} = {user_number * i}")