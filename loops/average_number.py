# Accept 10 numbers from user and display average of it.
numbers = []
total = 0
print("Enter 10 numbers to find averge.")
for i in range (4):
    num = int(input(f"Enter number {i+1}: "))  
    numbers.append(num) 
    total = sum(numbers)

print(total)
average = total / len(numbers)
print(average)