print("Program Started!")
print("Please enter a standard character:")
character = input()

if len(character) ==1:
    ascii_code = ord(character)
    print(f"The ASCII code for {character} is {ascii_code}")
else:
    print("Invalid input")

print("Program Ended!")
