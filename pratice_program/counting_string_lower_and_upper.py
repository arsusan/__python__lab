'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters: 3
No. of Lower case Characters : 12

Note: If you can take string input from user you can do it 
'''
def count_word(string):
    upper_count = 0
    lower_count = 0


    for string in user_input:
        if string.isupper():
            upper_count = upper_count + 1
        if string.islower():
            lower_count = lower_count + 1
        else:
            continue
    return lower_count, upper_count


user_input = input("Enter String: ")

user_input = list(user_input)
# print(user_input)
lower_count, upper_count = count_word(user_input)


print(f"Number of uppercase {upper_count}")
print(f"Number of lowercase {lower_count}")