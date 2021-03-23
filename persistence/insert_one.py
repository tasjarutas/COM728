import sqlite3


def get_bot_from_user():
    name = input("Please enter the name of the bot: ")
    maximum_speed = int(input("Please enter the maximum speed of the bot: "))
    maximum_strength = int(input("Please enter the maximum strength of the bot: "))
    date = input("Please enter the date of manufacture: ")
    manufacturer_id = int(input("Please enter manufacturer id: "))
    return [name, maximum_speed, maximum_strength, date, manufacturer_id]


def insert_bot_in_db(data):
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()

    sql = "INSERT INTO bots (name, maximum_speed, maximum_strength, date,manufacturer_id) VALUES (?, ?, ?, ?,?)"
    values = [data[0], data[1], data[2], data[3],data[4]]
    cursor.execute(sql, values)
    db.commit()
    row_id = cursor.lastrowid
    db.close()
    print("The record has been added to the database.")
    print(f"Id of new record is {row_id}")


def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)

if __name__ == "__main__":
    run()
