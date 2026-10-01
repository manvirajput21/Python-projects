# STUDENT MANAGEMENT SYSTEM PROJECT - 01

class student:

    def __init__(self, name, rollno, marks):
        """Student details are as follows"""
        self.name = name
        self.rollno = rollno
        self.marks = marks

        print('student "{}" & id "{}" & marks "{}"'.format( self.name, self.rollno, self.marks))


def add(students):
    name = input('ENTER NAME: ')
    rollno = int(input('ENTER ROLLNO OF STUDENT: '))
    marks = float(input('ENTER TOTAL MARKS OF STUDENT: '))

    students.append(student(name, rollno, marks))


def display(students):
    for i in students:
        print('Student name "{}" Student rollno "{}" Student marks "{}"'.format(
            i.name, i.rollno, i.marks
        ))


def searchstd(students):
    searchrollno = int(
        input('ENTER ROLLNO OF STUDENT YOU WANT TO SEARCH: ')
    )

    for i in students:
        if searchrollno == i.rollno:
            print('Student found:', i.name)
            return

    print('Student not found')


def updatestd(students):
    searchrollno = int(
        input('ENTER ROLLNO OF STUDENT YOU WANT TO SEARCH: ')
    )

    for i in students:
        if searchrollno == i.rollno:
            i.marks = float(input('UPDATE MARKS: '))
            i.name = input('UPDATE NAME: ')
            print('Student updated successfully')
            return

    print('Student not found')


def deletestd(students):
    searchrollno = int(
        input('ENTER ROLLNO OF STUDENT YOU WANT TO DELETE: ')
    )

    for i in students:
        if searchrollno == i.rollno:
            students.remove(i)
            print('Student deleted successfully')
            return

    print('Student not found')


def avgstd(students):
    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for i in students:
        total += i.marks

    average = total / len(students)

    print("Average Marks:", average)


def main():

    students = []

    while True:

        print('Menu')
        print(
            '\n1. ADD STUDENT'
            '\n2. DISPLAY STUDENT'
            '\n3. SEARCH STUDENT'
            '\n4. UPDATE STUDENT'
            '\n5. DELETE STUDENT'
            '\n6. AVERAGE MARKS'
            '\n7. EXIT'
        )

        choice = int(input('ENTER YOUR CHOICE: '))

        if choice == 1:
            add(students)

        elif choice == 2:
            display(students)

        elif choice == 3:
            searchstd(students)

        elif choice == 4:
            updatestd(students)

        elif choice == 5:
            deletestd(students)

        elif choice == 6:
            avgstd(students)

        elif choice == 7:
            print('EXIT')
            break

        else:
            print('INVALID CHOICE')


main()