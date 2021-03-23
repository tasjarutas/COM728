import sqlite3


def retrieve_bots():
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM bots;")
    all_records = cursor.fetchall()
    db.close()
    print("All bots in the system:")
    for bot in all_records:
        print(bot)


def run():
    retrieve_bots()


if __name__ == "__main__":
    run()
