print("What phrase do you see?")
text = input()

print("\nReversing ...")

print("The phrase is: ", end=" ")
for i in range(len(text)-1,-1,-1):
    print(f"{text[i]}", end="")
