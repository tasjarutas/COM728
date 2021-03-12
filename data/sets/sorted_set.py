def observed():
    observations = []
    for i in range(5):
        obj = input("Please enter an observation:")
        observations.append(obj)
    return observations


def remove_observations(observations_list):
    is_running = True

    while is_running:
        print("Do you wish to remove an observation (yes/no)?")
        response = input()
        if response == 'yes':
            remove_obj = input("What observation do you wish to remove?: ")
            observations_list.remove(remove_obj)
            print("Done!")
        else:
            is_running = False
    return observations_list

def run():
    objects = []
    update_list = []
    print("Counting observations...")
    objects = observed()
    updated_list = remove_observations(objects)

    print("Observations:")
    observations_set = set()
    for observation in updated_list :
        data = (observation, updated_list .count(observation))
        observations_set.add(data)
    # display set
    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")


if __name__ == '__main__':
    run()
