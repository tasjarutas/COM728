print("Please enter the first number")
first_number = int(input())
print("Please enter the second number")
second_number = int(input())

if first_number < second_number:
    print("The first number is the smallest")
elif second_number < first_number:
    print("The second number is the smallest")
else:
    print("Both are equal!")