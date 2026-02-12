class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("----- Student Info -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
        print("Average:", round(self.average_grade(), 2))
        print("------------------------")

def add_student(database):
    name = input("Enter student name: ").strip()

    while True:
        try:
            age = int(input("Enter student age: ").strip())
            if age < 0:
                print("Age cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for age.")

    while True:
        raw = input("Enter grades separated by space (or comma): ").strip()
        if raw == "":
            grades = []
            break
        raw = raw.replace(",", " ")
        parts = raw.split()
        try:
            grades = [float(x) for x in parts]
            break
        except ValueError:
            print("Please enter only numbers for grades (example: 80 90 75).")

    student = Student(name, age, grades)
    database.append(student)
    print("Student added.\n")

def display_all_students(database):
    if not database:
        print("No students in the database.\n")
        return

    print("\n=== All Students ===")
    for s in database:
        s.display_info()
    print()

def main():
    database = []

    print("Welcome to the Student Database System!\n")

    database.append(Student("Bob", 20, [88, 92, 79]))

    while True:
        print("Menu:")
        print("1) Add a new student")
        print("2) Display all students")
        print("3) Display averages only")
        print("4) Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_student(database)
        elif choice == "2":
            display_all_students(database)
        elif choice == "3":
            if not database:
                print("No students in the database.\n")
            else:
                print("\n=== Student Averages ===")
                for s in database:
                    print(f"{s.name}: {round(s.average_grade(), 2)}")
                print()
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please select 1-4.\n")
main()
