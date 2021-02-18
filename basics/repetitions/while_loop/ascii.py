print("How many bars should be charged?")
bars = int(input())
bars_charge=1
while bars_charge <= bars:
    print("Charging:", end=" ")
    print(f"{'❚'*bars_charge}")
    bars_charge +=1

print("The battery is fully charged.")
