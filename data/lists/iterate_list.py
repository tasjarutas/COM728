def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction_list = directions()
    for index in range(len(direction_list)):
        print("{}:{}.".format(index, direction_list[index]))


def run():
    menu()


if __name__ == '__main__':
    run()
