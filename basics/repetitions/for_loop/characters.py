print("What strange markings do you see?")
text = input()

print("Identifying ...\n")

for i in range(0,len(text)):
    print(f"index {i}: {text[i]}")

print("\nDone!")
