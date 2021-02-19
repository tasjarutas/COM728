print("How many numbers should I sum up?")
num_to_sum = int(input())

count = 1
sum = 0
while (count <= num_to_sum):
    print(f"Please enter number {count} of {num_to_sum}:")
    num = int(input())
    sum = sum+num
    count = count+1

print(f"The answer is {sum}.")
