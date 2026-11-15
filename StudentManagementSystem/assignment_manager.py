import json
import os

FILE_NAME = "assignments.json"


def load_assignments():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Could not read saved assignments.")
        return []


def save_assignments():
    with open(FILE_NAME, "w") as file:
        json.dump(assignments, file, indent=4)


assignments = load_assignments()


def add_assignment():
    subject = input("Enter subject: ")
    title = input("Enter assignment title: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    assignment = {
        "subject": subject,
        "title": title,
        "deadline": deadline,
        "status": "Pending"
    }

    assignments.append(assignment)
    save_assignments()
    print("Assignment added and saved successfully!")


def view_assignments():
    if len(assignments) == 0:
        print("No assignments available.")
        return

    for i, assignment in enumerate(assignments, start=1):
        print("\nAssignment", i)
        print("Subject:", assignment["subject"])
        print("Title:", assignment["title"])
        print("Deadline:", assignment["deadline"])
        print("Status:", assignment["status"])


def mark_submitted():
    if len(assignments) == 0:
        print("No assignments available.")
        return

    view_assignments()

    try:
        number = int(input("\nEnter assignment number: "))

        if 1 <= number <= len(assignments):
            assignments[number - 1]["status"] = "Submitted"
            save_assignments()
            print("Assignment marked as submitted!")
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_assignment():
    if len(assignments) == 0:
        print("No assignments available.")
        return

    view_assignments()

    try:
        number = int(input("\nEnter assignment number to delete: "))

        if 1 <= number <= len(assignments):
            deleted = assignments.pop(number - 1)
            save_assignments()
            print("Deleted assignment:", deleted["title"])
        else:
            print("Invalid assignment number.")

    except ValueError:
        print("Please enter a valid number.")


def search_assignment():
    if len(assignments) == 0:
        print("No assignments available.")
        return

    keyword = input("Enter subject or title to search: ").lower()
    found = False

    for assignment in assignments:
        if (keyword in assignment["subject"].lower()
                or keyword in assignment["title"].lower()):

            print("\nSubject:", assignment["subject"])
            print("Title:", assignment["title"])
            print("Deadline:", assignment["deadline"])
            print("Status:", assignment["status"])

            found = True

    if not found:
        print("No matching assignment found.")




def filter_assignments(status):
    found = False

    for assignment in assignments:
        if assignment["status"] == status:

            print("\nSubject:", assignment["subject"])
            print("Title:", assignment["title"])
            print("Deadline:", assignment["deadline"])
            print("Status:", assignment["status"])

            found = True

    if not found:
        print("No", status, "assignments found.")


while True:
    print("\n===== ASSIGNMENT MANAGER =====")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark Assignment as Submitted")
    print("4. Delete Assignment")
    print("5. Search Assignment")
    print("6. Filter Assignments by Status")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_assignment()

    elif choice == "2":
        view_assignments()

    elif choice == "3":
        mark_submitted()

    elif choice == "4":
        delete_assignment()

    elif choice == "5":
        search_assignment()

    elif choice == "6":
        print("\n1. Pending Assignments")
        print("2. Submitted Assignments")

        status_choice = input("Choose status: ")

        if status_choice == "1":
            filter_assignments("Pending")

        elif status_choice == "2":
            filter_assignments("Submitted")

        else:
            print("Invalid status choice.")

    elif choice == "7":
        print("Thank you for using Assignment Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
