print("What level of brightness is required?")
brightness = int(input())

print("Adjusting brightness ...")
for level in range(2,brightness+2,2):
    print(f"Beep's brightness level: {'*'*level}")
    print(f"Bop's brightness level: {'*'*level}\n")

print("Adjustments complete!")

