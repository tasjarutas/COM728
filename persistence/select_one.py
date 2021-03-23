import sqlite3


def retrieve_bot():
    db = sqlite3.connect("../persistence/sqlite/bots.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM bots;")
    single_record = cursor.fetchone()
    db.close()
    print(single_record)


def run():
    retrieve_bot()


if __name__ == "__main__":
    run()
