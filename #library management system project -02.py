
# Library Management System - Project 02

class library:
    def __init__(self, bookid, name):
        self.bookid = bookid
        self.name = name
        self.issued = False


def addbooks(Books):
    name = input("Enter name of book: ")
    bookid = int(input("Enter book ID: "))

    for i in Books:
        if i.bookid == bookid:
            print("BOOK ID ALREADY EXISTS")
            return

    Books.append(library(bookid, name))
    print("BOOK ADDED SUCCESSFULLY")


def searchbooks(Books):
    searchid = int(input("Search book by book ID: "))

    for i in Books:
        if searchid == i.bookid:
            print("\nBook Found!")
            print("Book ID:", i.bookid)
            print("Book Name:", i.name)

            if i.issued:
                print("Status: Issued")
            else:
                print("Status: Available")
            return

    print("BOOK NOT FOUND")


def issuebooks(Books):
    bookid = int(input("Enter book ID you want to issue: "))

    for i in Books:
        if bookid == i.bookid:
            if i.issued:
                print("BOOK ALREADY ISSUED")
            else:
                i.issued = True
                print("BOOK ISSUED SUCCESSFULLY!")
            return

    print("BOOK NOT FOUND")


def returnbooks(Books):
    bookid = int(input("Enter book ID you want to return: "))

    for i in Books:
        if bookid == i.bookid:
            if i.issued:
                i.issued = False
                print("BOOK RETURNED SUCCESSFULLY")
            else:
                print("BOOK IS NOT ISSUED")
            return

    print("BOOK NOT FOUND")


def displaybooks(Books):
    found = False

    for i in Books:
        if not i.issued:
            print("Book ID:", i.bookid)
            print("Book Name:", i.name)
            print("----------------------")
            found = True

    if not found:
        print("NO AVAILABLE BOOKS")


def records(Books):
    print("\n--- LIBRARY RECORDS ---")

    if len(Books) == 0:
        print("No books in library.")
        return

    for i in Books:
        print("Book ID:", i.bookid)
        print("Book Name:", i.name)

        if i.issued:
            print("Status: Issued")
        else:
            print("Status: Available")

        print("----------------------")


def main():
    Books = []

    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. ADD BOOK")
        print("2. SEARCH BOOK")
        print("3. ISSUE BOOK")
        print("4. RETURN BOOK")
        print("5. DISPLAY AVAILABLE BOOKS")
        print("6. RECORDS")
        print("7. EXIT")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            addbooks(Books)

        elif choice == 2:
            searchbooks(Books)

        elif choice == 3:
            issuebooks(Books)

        elif choice == 4:
            returnbooks(Books)

        elif choice == 5:
            displaybooks(Books)

        elif choice == 6:
            records(Books)

        elif choice == 7:
            print("EXIT")
            break

        else:
            print("INVALID CHOICE")


main()
