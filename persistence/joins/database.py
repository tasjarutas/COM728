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