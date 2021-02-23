print("Please enter a sequence")
sequence = input()

print("Please enter the character for the marker")
marker = input()

is_counting = False
count = 0

for character in sequence:
    if is_counting == False and character == marker:
        is_counting = True
    elif is_counting == True and character== marker:
        print("found the second marker")
    elif is_counting:
        count+=1

print(f"The distance between the markers is {count}")
