def sum_weights(weight_beep,weight_bop):
    total_weight = weight_beep+weight_bop
    return total_weight

def calc_avg_weight(weight_beep,weight_bop):
    average_weight = sum_weights(weight_beep,weight_bop)/2
    return average_weight
def run():
    print("What is the weight of Beep?")
    weight_beep = int(input())
    print("What is the weight of Bop?")
    weight_bop = int(input())
    print("What would you like to calculate (sum or average)?")
    choice = input()
    if choice == "sum":
        sum = sum_weights(weight_beep,weight_bop)
        print(f"The sum of Beep and Bop's weight is {sum}")
    elif choice == "average":
        avg = calc_avg_weight(weight_beep,weight_bop)
        print(f"The average of Beep and Bop's weight is {avg}")
    else:
        print("Invalid calculation")


run()


