import sqlite3


def get_bot_id_from_user():
    bot_id = input("Please enter a bot id: ")
    return bot_id


def display_bot_from_db(bot_id):
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM bots WHERE id=?"
    values = [bot_id]
    cursor.execute(sql, values)
    record = cursor.fetchone()
    db.close()

    print(record)


def get_bot_details_from_user():
    print("What would you like to change:")
    field = input()
    print(f"What is the new value for {field}:")
    value = int(input())
    return [field, value]


def update_bot_in_db(data, bot_id):
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()
    sql = "UPDATE bots SET " + str(data[0]) + " = " + str(data[1]) + " WHERE id = " + bot_id
    # values = [data[0], data[1], bot_id]
    cursor.execute(sql)
    db.commit()
    db.close()

    print("Updated")


def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)

    data = get_bot_details_from_user()
    update_bot_in_db(data, bot_id)


if __name__ == "__main__":
    run()
