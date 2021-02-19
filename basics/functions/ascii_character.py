print("Program Started!")
print("Please enter an ASCII code:")
ascii_code = abs(int(input()))

if ascii_code in range(32,127):
    character = chr(ascii_code)
    print(f"The character represented by the ASCII code {ascii_code} is {character}")
else:
    print("Invalid ASCII code")

print("Program Ended!")
