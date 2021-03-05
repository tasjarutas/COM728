def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    paths = movements()
    print(f"{paths[0]} for {paths[1]} steps")
    print(f"{paths[2]} for {paths[3]} steps")
    print(f"{paths[4]} for {paths[5]} steps")
    print(f"{paths[6]} for {paths[7]} steps")

    for i in range(0,len(paths),2):
        print(f"{paths[i]} for {paths[i+1]} steps")


if __name__ == '__main__':
    run()
