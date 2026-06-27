# ==========================================
# LIBRARY MANAGEMENT SYSTEM
# File Name: library_management.py
# ==========================================

from datetime import datetime, timedelta

# Master Dictionary
library = {
    "978-111": {
        "title": "Python Programming",
        "author": "John Smith",
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    },
    "978-222": {
        "title": "Data Structures",
        "author": "Ramesh Kumar",
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    },
    "978-333": {
        "title": "Machine Learning",
        "author": "Andrew Ng",
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    },
    "978-444": {
        "title": "Database Systems",
        "author": "Korth",
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    },
    "978-555": {
        "title": "Computer Networks",
        "author": "Forouzan",
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    }
}


# Function to calculate due date
def check_due_date(issue_date):
    due_date = issue_date + timedelta(days=7)
    return due_date.strftime("%d-%B-%Y")


# Function to add book
def add_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn in library:
        print("Book with this ISBN already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    }

    print("Book Added Successfully!")


# Function to issue book
def issue_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn not in library:
        print("Invalid ISBN!")
        return

    if not library[isbn]["available"]:
        print("Book is already issued!")
        return

    student_id = input("Enter Borrower ID: ")
    borrower = input("Enter Borrower Name: ")

    issue_date = datetime.now()

    library[isbn]["available"] = False
    library[isbn]["borrower"] = borrower
    library[isbn]["student_id"] = student_id
    library[isbn]["issue_date"] = issue_date

    print("\nBook Issued Successfully!")
    print("Title :", library[isbn]["title"])
    print("Due Date :", check_due_date(issue_date))


# Function to return book
def return_book():
    isbn = input("Enter ISBN: ").strip()

    if isbn not in library:
        print("Invalid ISBN!")
        return

    if library[isbn]["available"]:
        print("Book is already available in library!")
        return

    issue_date = library[isbn]["issue_date"]

    if issue_date:
        days = (datetime.now() - issue_date).days

        if days > 7:
            fine = (days - 7) * 2
            print("Overdue Fine: Rs.", fine)

    library[isbn]["available"] = True
    library[isbn]["borrower"] = None
    library[isbn]["student_id"] = None
    library[isbn]["issue_date"] = None

    print("Book Returned Successfully!")


# Function to search book
def search_book():
    keyword = input("Enter Title or Author: ").lower().strip()

    found = False

    for isbn, details in library.items():

        if (keyword in details["title"].lower() or
                keyword in details["author"].lower()):

            found = True

            print("\nISBN:", isbn)
            print("Title:", details["title"])
            print("Author:", details["author"])
            print("Status:",
                  "Available" if details["available"] else "Issued")

    if not found:
        print("No matching book found!")


# Function to view catalog
def view_catalog():

    if not library:
        print("Library is empty!")
        return

    print("\n================ LIBRARY CATALOG ================")

    print("{:<12} {:<25} {:<20} {:<12}".format(
        "ISBN", "TITLE", "AUTHOR", "STATUS"))

    print("-" * 75)

    for isbn, details in library.items():

        status = "Available" if details["available"] else "Issued"

        print("{:<12} {:<25} {:<20} {:<12}".format(
            isbn,
            details["title"],
            details["author"],
            status
        ))


# Function to count books
def book_statistics():

    available = 0
    issued = 0

    for book in library.values():

        if book["available"]:
            available += 1
        else:
            issued += 1

    print("\nTotal Books :", len(library))
    print("Available Books :", available)
    print("Issued Books :", issued)


# Function to export catalog
def export_catalog():

    file = open("library_catalog.txt", "w")

    file.write("LIBRARY CATALOG\n")
    file.write("=" * 60 + "\n")

    for isbn, details in library.items():

        status = "Available" if details["available"] else "Issued"

        file.write(
            f"{isbn} | {details['title']} | {details['author']} | {status}\n")

    file.close()

    print("Catalog exported to library_catalog.txt")


# Main Program
while True:

    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Book Statistics")
    print("7. Export Catalog")
    print("8. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            issue_book()

        elif choice == 3:
            return_book()

        elif choice == 4:
            search_book()

        elif choice == 5:
            view_catalog()

        elif choice == 6:
            book_statistics()

        elif choice == 7:
            export_catalog()

        elif choice == 8:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number!")