import json


def read(file_name):
    with open(file_name) as file:
        data = json.load(file)
        # display the name of the city
        city_name = data["city"]
        print(f"City Name: {city_name}")
        population = data["population"]
        print(f"Population size: {population}")
        # display the name of each bot
        bots = data["bots"]
        for bot in bots:
            bot_name = bot["name"]
            bot_speed = bot["stats"]["speed"]
            bot_strength = bot["stats"]["strength"]
            print(f"{bot_name} has a strength level of {bot_strength} and a speed level of {bot_speed}")


def run():
    read("robocity.json")

if __name__ == "__main__":
    run()
