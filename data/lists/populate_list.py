def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction_list = directions()
    for index in range(len(direction_list)):
        print(f"{index}:{direction_list[index]}.")

    response = int(input())
    return direction_list[response]


def run():
    route = []
    print("Working out escape route...")
    for i in range(5):
        direction = menu()
        route.append(direction)
    print(f"Escape route: {route}")


if __name__ == '__main__':
    run()
