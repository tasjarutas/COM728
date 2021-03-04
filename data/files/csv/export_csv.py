import csv


def export(file_name, num_bots):
    names=[]
    print ("Exporting...")
    with open(file_name, "a") as file:
        for i in range(num_bots):
            bot_id = int(input("Please enter the bot id: "))
            bot_name = input("Please enter the bot name: ")
            bot_paint = input("Please enter the bot paint: ")
            file.write(f"{bot_id},{bot_name},{bot_paint}\n")
    print("Done!")



def run():
    export("exported_bots.csv",2)


if __name__ == "__main__":
    run()
