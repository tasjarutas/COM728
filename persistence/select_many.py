import sqlite3


def retrieve_bots(number_bots=None):
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM bots;")
    if number_bots is None:
        print("All bots in the system:")
        records = cursor.fetchall()
    else:
        print(f"First {number_bots} bots in the system:")
        records = cursor.fetchmany(number_bots)
    db.close()

    for bot in records:
        print(bot)


def run():
    retrieve_bots()
    retrieve_bots(2)


if __name__ == "__main__":
    run()
