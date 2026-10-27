# LIBRARY MANAGEMENT SYSTEM

books = [
    ["Python Programming", "Available"],
    ["Data Structures", "Available"],
    ["Database Management", "Available"]
]


def display_books():
    print("\n--- BOOK LIST ---")

    if len(books) == 0:
        print("No books available.")
    else:
        for i in range(len(books)):
            print(i + 1, ".", books[i][0], "-", books[i][1])


def add_book():
    name = input("Enter book name: ")

    if name != "":
        books.append([name, "Available"])
        print("Book added successfully.")
    else:
        print("Book name cannot be empty.")


def search_book():
    name = input("Enter book name to search: ")
    found = False

    for book in books:
        if book[0].lower() == name.lower():
            print("Book found!")
            print("Book:", book[0])
            print("Status:", book[1])
            found = True
            break

    if not found:
        print("Book not found.")


def issue_book():
    display_books()

    if len(books) > 0:
        choice = int(input("Enter book number to issue: "))

        if choice >= 1 and choice <= len(books):
            if books[choice - 1][1] == "Available":
                books[choice - 1][1] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
        else:
            print("Invalid book number.")


def return_book():
    display_books()

    if len(books) > 0:
        choice = int(input("Enter book number to return: "))

        if choice >= 1 and choice <= len(books):
            if books[choice - 1][1] == "Issued":
                books[choice - 1][1] = "Available"
                print("Book returned successfully.")
            else:
                print("This book was not issued.")
        else:
            print("Invalid book number.")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_books()

        elif choice == 2:
            add_book()

        elif choice == 3:
            search_book()

        elif choice == 4:
            issue_book()

        elif choice == 5:
            return_book()

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
