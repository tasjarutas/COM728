print("What phrase do you see?")
text_list = input()

print("\nReversing ...")

print("The phrase is: ", end=" ")
reseversed = ""
for letter in text_list:
    reseversed = letter+reseversed

print(reseversed)
