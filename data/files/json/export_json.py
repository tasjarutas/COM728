import json


def read(file_name):
    print("Reading...", end="")
    with open(file_name) as file:
        data = json.load(file)
        print("Done!")
    return data


def save(file_name, json_data):
    print("Exporting...", end="")
    with open(file_name, "w") as file:
        json.dump(json_data, file, indent = 4)
        print("Done!")

def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)

if __name__ == "__main__":
    run()
