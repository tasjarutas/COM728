def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def display_keys(data):
    print("Keys:")
    for key in data.keys():
        print (key)

def display_values(data):
    print("Values")
    for value in data.values():
        print(value)


def display_items(data):
    print("Paris:")
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    data = pattern()
    print("Dictionary:")
    print(data)
    display_keys(data)
    display_values(data)
    display_items(data)



if __name__ == '__main__':
    run()
