# ==========================================
# INVENTORY MANAGEMENT SYSTEM
# File Name: inventory_management.py
# ==========================================

from datetime import datetime

inventory = {}
transaction_log = []


# Load Inventory from File
def load_inventory():
    try:
        file = open("inventory.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 6:
                pid, name, category, price, quantity, reorder = data

                inventory[pid] = {
                    "name": name,
                    "category": category,
                    "price": float(price),
                    "quantity": int(quantity),
                    "reorder_level": int(reorder)
                }

        file.close()

    except FileNotFoundError:
        print("No inventory file found. Starting with empty inventory.")


# Save Inventory
def save_inventory():
    file = open("inventory.txt", "w")

    for pid, product in inventory.items():
        file.write(
            f"{pid},{product['name']},{product['category']},"
            f"{product['price']},{product['quantity']},"
            f"{product['reorder_level']}\n"
        )

    file.close()


# Log Transactions
def log_transaction(pid, action, qty):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    transaction_log.append({
        "time": time,
        "product_id": pid,
        "action": action,
        "quantity": qty
    })


# Add Product
def add_product():

    pid = input("Enter Product ID (P001): ").upper()

    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")

    try:
        price = float(input("Enter Unit Price: "))
        quantity = int(input("Enter Quantity: "))
        reorder = int(input("Enter Reorder Level: "))

        inventory[pid] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "reorder_level": reorder
        }

        print("Product Added Successfully!")

    except ValueError:
        print("Invalid Input!")


# Stock In
def stock_in():

    pid = input("Enter Product ID: ").upper()

    if pid not in inventory:
        print("Product not found!")
        return

    try:
        qty = int(input("Enter Quantity to Add: "))

        inventory[pid]["quantity"] += qty

        log_transaction(pid, "IN", qty)

        print("Stock Updated Successfully!")

    except ValueError:
        print("Invalid Quantity!")


# Stock Out
def stock_out():

    pid = input("Enter Product ID: ").upper()

    if pid not in inventory:
        print("Product not found!")
        return

    try:
        qty = int(input("Enter Quantity to Remove: "))

        if qty > inventory[pid]["quantity"]:
            print("Insufficient Stock!")
            return

        inventory[pid]["quantity"] -= qty

        log_transaction(pid, "OUT", qty)

        print("Stock Removed Successfully!")

    except ValueError:
        print("Invalid Quantity!")


# View Inventory
def view_inventory():

    if not inventory:
        print("Inventory is empty!")
        return

    print("\n================ INVENTORY =================")

    print("{:<8} {:<20} {:<15} {:<10} {:<10} {:<12}".format(
        "ID", "NAME", "CATEGORY",
        "PRICE", "QTY", "VALUE"
    ))

    print("-" * 80)

    for pid, product in inventory.items():

        value = product["price"] * product["quantity"]

        print("{:<8} {:<20} {:<15} {:<10.2f} {:<10} {:<12.2f}".format(
            pid,
            product["name"],
            product["category"],
            product["price"],
            product["quantity"],
            value
        ))


# Low Stock Alert
def low_stock_alert():

    found = False

    print("\n========= LOW STOCK ITEMS =========")

    for pid, product in inventory.items():

        if product["quantity"] <= product["reorder_level"]:

            found = True

            print(
                pid,
                "-",
                product["name"],
                "(Qty:",
                product["quantity"],
                ")"
            )

    if not found:
        print("No low stock items.")


# Total Inventory Value
def get_total_value():

    total = 0

    for product in inventory.values():
        total += product["price"] * product["quantity"]

    return total


# Search Product (Bonus)
def search_product():

    keyword = input(
        "Enter Product Name or Category: "
    ).lower()

    found = False

    for pid, product in inventory.items():

        if (keyword in product["name"].lower()
                or keyword in product["category"].lower()):

            found = True

            print("\nProduct ID:", pid)
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

    if not found:
        print("No matching product found!")


# Transaction History
def show_transactions():

    if not transaction_log:
        print("No transactions found!")
        return

    print("\n========== TRANSACTION LOG ==========")

    for t in transaction_log:

        print(
            t["time"],
            "|",
            t["product_id"],
            "|",
            t["action"],
            "| Qty:",
            t["quantity"]
        )


# Inventory Report
def generate_report():

    total_products = len(inventory)

    total_value = get_total_value()

    categories = set()

    low_stock_count = 0

    highest_value = 0
    highest_product = None

    for pid, product in inventory.items():

        categories.add(product["category"])

        if product["quantity"] <= product["reorder_level"]:
            low_stock_count += 1

        value = product["price"] * product["quantity"]

        if value > highest_value:
            highest_value = value
            highest_product = product["name"]

    print("\n========== INVENTORY REPORT ==========")

    print("Total Products :", total_products)

    print("Total Stock Value : Rs.", round(total_value, 2))

    print("Categories :", ", ".join(categories))

    print("Low Stock Items :", low_stock_count)

    if highest_product:
        print(
            "Highest Value Item :",
            highest_product,
            "(Rs.",
            round(highest_value, 2),
            ")"
        )


# Main Program
load_inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Inventory Report")
    print("7. Search Product")
    print("8. Transaction Log")
    print("9. Save & Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_product()

        elif choice == 2:
            stock_in()

        elif choice == 3:
            stock_out()

        elif choice == 4:
            view_inventory()

        elif choice == 5:
            low_stock_alert()

        elif choice == 6:
            generate_report()

        elif choice == 7:
            search_product()

        elif choice == 8:
            show_transactions()

        elif choice == 9:
            save_inventory()
            print("Inventory Saved Successfully!")
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number!")