name = input("What is your name human?\n")
age = int(input("How old are you (in years)?\n"))
height = float(input("How tall are you (in meters)?\n"))
weight = float(input("How much do you weigh (in kilograms)?\n"))
bmi = weight/height**2
print (f"{name}, you are {age} years old and your bmi is {bmi:.2f}")