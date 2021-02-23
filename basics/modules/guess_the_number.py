import random as rnd

print("Please enter the minimum value:")
minimum_value = int(input())
print("Please enter the maximum value:")
maximum_value = int(input())

random_number = rnd.randrange(minimum_value,maximum_value)
correct=False
print(f"I am thinking of a number between {minimum_value} and {maximum_value}. Can you guess what it is?")
while(correct != True):
    guess = int(input())
    if guess < random_number:
        print("Your guess is too low.")
        print("Try again:\n")
    elif guess > random_number:
        print("Your guess is too high.")
        print("Try again:")
    else:
        print("Congratulations! You guessed my number!")
        correct = True

