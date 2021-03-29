import database


def menu():
    print("Please select one of the following options: ")
    print("[1] Display stock levels")
    print("[2] Display suppliers")
    print("[3] Display supplier locations")
    selection = int(input("Your selection: "))
    return selection


def run():
    option = menu()
    if option == 1:
        database.display_products_with_stock_levels()
    elif option == 2:
        database.display_product_supplier()
    elif option == 3:
        database.display_product_supplier_locations()


if __name__ == '__main__':
    run()