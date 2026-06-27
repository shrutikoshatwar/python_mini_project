'''Initialize an empty dictionary to store student records.
8. Display a menu: Add / View All / Search / Update / Delete / Exit.
9. Accept user menu choice with input validation.
10. For Add: take name, roll number, and 5 subject marks. Calculate percentage and grade.
Store in dictionary with roll number as key.
11. For View: iterate through dictionary and print all records in formatted table.
12. For Search: prompt roll number, look up dictionary, print record if found.
13. For Update: find record by roll number, allow field-by-field update.
14. For Delete: confirm deletion, then remove entry from dictionary.
15. Repeat menu until user selects Exit.'''
# Creating empty dictionary
student = {}

while True:
    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1. Add")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter name of student: ")
        roll_no = int(input("Enter Roll No: "))

        print("Enter 5 subject marks:")
        s1 = int(input("Subject 1: "))
        s2 = int(input("Subject 2: "))
        s3 = int(input("Subject 3: "))
        s4 = int(input("Subject 4: "))
        s5 = int(input("Subject 5: "))

        total = s1 + s2 + s3 + s4 + s5
        percentage = (total / 500) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student[roll_no] = {
            "name": name,
            "Roll no": roll_no,
            "percentage": percentage,
            "grade": grade
        }

        print("New student added successfully!")

    # View All
    elif choice == "2":
        if not student:
            print("No records found!")
        else:
            print("\nStudent Records:")
            print("-" * 40)

            for key, value in student.items():
                print("Roll No:", value["Roll no"])
                print("Name:", value["name"])
                print("Percentage:", round(value["percentage"], 2))
                print("Grade:", value["grade"])
                print("-" * 40)

    # Search
    elif choice == "3":
        roll_no = int(input("Enter Roll No to search: "))

        if roll_no in student:
            details = student[roll_no]

            print("\nRecord Found!")
            print("Name:", details["name"])
            print("Roll No:", details["Roll no"])
            print("Percentage:", round(details["percentage"], 2))
            print("Grade:", details["grade"])
        else:
            print("Record not found!")

    # Update
    elif choice == "4":
        roll_no = int(input("Enter Roll No to update: "))

        if roll_no in student:
            new_name = input("Enter new name: ")
            new_roll = int(input("Enter new Roll No: "))

            student[new_roll] = student.pop(roll_no)
            student[new_roll]["name"] = new_name
            student[new_roll]["Roll no"] = new_roll

            print("Record updated successfully!")
            print(student[new_roll])

        else:
            print("Roll No not found!")

    # Delete
    elif choice == "5":
        roll_no = int(input("Enter Roll No to delete: "))

        if roll_no in student:
            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                del student[roll_no]
                print("Record deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Roll No not found!")

    # Exit
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")