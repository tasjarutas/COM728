def observed():
    observations = []
    for i in range(7):
        obj = input("Please enter an observation:")
        observations.append(obj)
    return observations


def run():
    objects = []
    print("Counting observations...")
    objects = observed()
    observation_set = set()
    for obj in objects:
        data = (obj, objects.count(obj))
        observation_set.add(data)

    for data in observation_set:
        print(f"{data[0]} observed {data[1]} times.")


if __name__ == '__main__':
    run()
