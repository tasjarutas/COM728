print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
columns = int(input())

print("Here I go: ")
for i in range(0,rows):
    for j in range(0,columns):
        print(":-) ", end="")
    print("")
print("\nDone!")
