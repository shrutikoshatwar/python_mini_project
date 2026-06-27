expenses = []

# Set monthly budget
while True:
    try:
        budget = float(input("Enter Monthly Budget (Rs.): "))
        if budget > 0:
            break
        else:
            print("Budget must be greater than 0.")
    except ValueError:
        print("Enter a valid amount!")


# Function to validate amount
def validate_amount():
    while True:
        try:
            amount = float(input("Enter Amount (Rs.): "))
            if amount > 0:
                return amount
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount!")


# Add Expense
def add_expense():
    description = input("Enter Description: ")
    category = input(
        "Enter Category (Food/Travel/Bills/Entertainment/Other): ")
    amount = validate_amount()
    date = input("Enter Date (DD-MM-YYYY): ")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    total = sum(exp["amount"] for exp in expenses)

    print("\nExpense Added Successfully!")
    print("Running Total: Rs.", round(total, 2))


# View Expenses
def view_expenses():

    if not expenses:
        print("No expenses recorded!")
        return

    print("\n================ EXPENSE LIST ================")

    print("{:<5} {:<20} {:<15} {:<12} {:<12}".format(
        "No", "Description", "Category", "Amount", "Date"))

    print("-" * 70)

    for i, exp in enumerate(expenses, start=1):
        print("{:<5} {:<20} {:<15} {:<12.2f} {:<12}".format(
            i,
            exp["description"],
            exp["category"],
            exp["amount"],
            exp["date"]
        ))


# Category Summary
def category_summary():

    if not expenses:
        print("No expenses recorded!")
        return

    summary = {}

    for exp in expenses:
        category = exp["category"]

        if category in summary:
            summary[category] += exp["amount"]
        else:
            summary[category] = exp["amount"]

    print("\n=========== CATEGORY SUMMARY ===========")

    for category, total in summary.items():
        print(f"{category:<15} : Rs. {total:.2f}")


# Top Spending Category
def get_top_category():

    if not expenses:
        return None

    summary = {}

    for exp in expenses:
        category = exp["category"]

        if category in summary:
            summary[category] += exp["amount"]
        else:
            summary[category] = exp["amount"]

    top_category = max(summary, key=summary.get)

    return top_category, summary[top_category]


# Budget Report
def budget_report():

    total_spent = sum(exp["amount"] for exp in expenses)

    remaining = budget - total_spent

    percent_used = (total_spent / budget) * 100

    print("\n========== BUDGET REPORT ==========")
    print(f"Total Spent : Rs. {total_spent:.2f}")
    print(f"Budget Limit : Rs. {budget:.2f}")
    print(f"Remaining : Rs. {remaining:.2f}")
    print(f"Used : {percent_used:.2f}%")

    if percent_used >= 100:
        print(" DANGER: Budget Exceeded!")
    elif percent_used >= 80:
        print(" WARNING: More than 80% budget used.")
    else:
        print(" Budget is under control.")

    top = get_top_category()

    if top:
        print(f"Top Category : {top[0]} (Rs. {top[1]:.2f})")


# Filter by Category (Bonus)
def filter_category():

    category = input("Enter Category: ")

    found = False

    print("\nExpenses in Category:", category)

    for exp in expenses:

        if exp["category"].lower() == category.lower():

            found = True

            print(
                exp["description"],
                "- Rs.",
                exp["amount"],
                "-",
                exp["date"]
            )

    if not found:
        print("No records found.")


# Most Expensive Expense (Bonus)
def most_expensive():

    if not expenses:
        print("No expenses recorded!")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print("\n====== MOST EXPENSIVE EXPENSE ======")
    print("Description :", highest["description"])
    print("Category :", highest["category"])
    print("Amount : Rs.", highest["amount"])
    print("Date :", highest["date"])


# Save to File (Bonus)
def save_to_file():

    file = open("expenses.txt", "w")

    file.write("PERSONAL EXPENSE REPORT\n")
    file.write("=" * 60 + "\n")

    for exp in expenses:
        file.write(
            f"{exp['description']} | "
            f"{exp['category']} | "
            f"{exp['amount']} | "
            f"{exp['date']}\n"
        )

    file.close()


# Main Program
while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("Monthly Budget: Rs.", budget)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Filter by Category")
    print("6. Most Expensive Expense")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            category_summary()

        elif choice == 4:
            budget_report()

        elif choice == 5:
            filter_category()

        elif choice == 6:
            most_expensive()

        elif choice == 7:
            save_to_file()
            print("Expense data saved to expenses.txt")
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number!")