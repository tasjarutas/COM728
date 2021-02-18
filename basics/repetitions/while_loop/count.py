print("How many live cables should I avoid?")
live_cables = int(input())
count = 0

while count < live_cables:
    print(f"Avoiding... ", end=" ")
    print("Done! {count+1} live cables avoided. ")
    count +=1

print("All live cables have been avoided.")