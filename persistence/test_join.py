import sqlite3


def display_users():
    db = sqlite3.connect("../persistence/sqlite/users.db")
    cursor = db.cursor()

    sql = """SELECT first_name, last_name, organisation.name
        FROM user 
        LEFT OUTER JOIN organisation ON user.organisation_id = organisation_id"""
    cursor.execute(sql)
    db.close()
