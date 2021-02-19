print("Please enter a number: ")
num = int(input())
count = 1
factorial = 1
while count <= num:
    factorial = factorial*count
    count = count+1

print(f"The factorial is {factorial}.")
