import sqlite3
import os


def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = "SELECT name, description, stock.quantity " \
          "FROM product NATURAL JOIN stock"
    cursor.execute(sql)
    all_records = cursor.fetchall()
    db.close()
    num_records = len(all_records)
    print(f"There are {num_records} products in the catalogue.")
    print("The stock level for each product is as follows: ")
    for record in all_records:
        print(f"Product: {record[0]}")
        print(f"Description: {record[1]}")
        print(f"Stock level: {record[2]}")


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = """SELECT product.name, supplier.name
            FROM product 
            INNER JOIN supplier  ON product.supplier_id = supplier.id"""
    cursor.execute(sql)
    all_records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows: ")
    for record in all_records:
        print(f"Product: {record[0]}", end=', ')
        print(f"Supplier: {record[1]}")


def display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = """SELECT product.name, supplier.name, location.city, location.country
FROM product 
INNER JOIN supplier  ON product.supplier_id = supplier.id
INNER JOIN location ON supplier.location_id = location.id"""
    cursor.execute(sql)
    all_records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows: ")
    for record in all_records:
        print(f"Product: {record[0]}", end=', ')
        print(f"Supplier: {record[1]}", end =', ')
        print(f"Supplier Location: {record[2]}", end=', ')
        print(f"{record[3]}")


def display_products_missing_suppliers():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = """SELECT product.name, supplier.name, location.city, location.country
FROM product 
LEFT OUTER JOIN supplier  ON product.supplier_id = supplier.id
LEFT OUTER JOIN location ON supplier.location_id = location.id"""
    cursor.execute(sql)
    all_records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows: ")
    for record in all_records:
        print(f"Product: {record[0]}", end=', ')
        print(f"Supplier: {record[1]}", end=', ')
        print(f"Supplier Location: {record[2]}", end=', ')
        print(f"{record[3]}")


def display_suppliers_missing_products():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = """SELECT product.name, supplier.name
FROM supplier 
LEFT OUTER JOIN product ON supplier.id  = product.supplier_id 
"""
    cursor.execute(sql)
    all_records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows: ")
    for record in all_records:
        print(f"Supplier: {record[1]}", end=', ')
        print(f"Product: {record[0]}")


def display_missing_data():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql1 = """SELECT product.name, supplier.name
FROM product
LEFT OUTER JOIN supplier  ON product.supplier_id = supplier.id
UNION
SELECT product.name, supplier.name
FROM supplier 
LEFT OUTER JOIN product ON supplier.id  = product.supplier_id
    """

    sql2 = """SELECT supplier.name, location.city, location.country
FROM supplier
LEFT OUTER JOIN location  ON supplier.location_id = location.id
UNION
SELECT supplier.name, location.city, location.country
FROM location
LEFT OUTER JOIN supplier ON location.id = supplier.location_id"""
    cursor.execute(sql1)
    all_records01 = cursor.fetchall()
    cursor.execute(sql2)
    all_records02 = cursor.fetchall()
    db.close()
    #print(all_records)
    print(f"The following products are missing suppliers:")
    for record in all_records01:
        if record[1] == None:
            print(f"{record[0]}")
    print(f"The following suppliers are missing products:")
    for record in all_records01:
        if record[0] == None:
            print(f"{record[1]}")

    print(f"The following locations are not associated with a supplier:")
    for record in all_records02:
        if record[0] == None:
            print(f"{record[1]}", end=', ')
            print(f"{record[2]}")