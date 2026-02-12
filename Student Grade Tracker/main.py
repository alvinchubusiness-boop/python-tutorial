import os

FILENAME = "grades.txt"


def load_grades(filename=FILENAME):
    """Load grades from file. Returns a dict: {subject: grade}."""
    grades = {}
    if not os.path.exists(filename):
        return grades

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # expected format: Subject,Grade
                parts = line.split(",", 1)
                if len(parts) != 2:
                    continue
                subject = parts[0].strip()
                try:
                    grade = float(parts[1].strip())
                except ValueError:
                    continue

                grades[subject] = grade
    except (OSError, IOError) as e:
        print(f"[File Error] Could not read file: {e}")

    return grades


def save_grades(grades, filename=FILENAME):
    """Save grades dict to file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for subject, grade in grades.items():
                f.write(f"{subject},{grade}\n")
    except (OSError, IOError) as e:
        print(f"[File Error] Could not write file: {e}")


def calculate_average(grades):
    """Return average grade, or None if no grades."""
    if not grades:
        return None
    return sum(grades.values()) / len(grades)


def get_grade_input(subject):
    """Keep asking until user enters a valid grade (0-100)."""
    while True:
        raw = input(f"Enter grade for {subject} (0-100): ").strip()
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 85 or 92.5).")


def main():
    print("=== Student Grade Tracker ===")

    # Step: read existing grades
    grades = load_grades()
    if grades:
        print("\nLoaded grades from file:")
        for sub, g in grades.items():
            print(f"  {sub}: {g}")
    else:
        print("\nNo saved grades found yet.")

    while True:
        print("\nMenu:")
        print("1) Add/Update a grade")
        print("2) View grades and average")
        print("3) Save grades to file")
        print("4) Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            subject = input("Enter subject name: ").strip()
            if not subject:
                print("Subject name cannot be empty.")
                continue
            grade = get_grade_input(subject)
            grades[subject] = grade
            print(f"Saved in memory: {subject} = {grade}")

        elif choice == "2":
            if not grades:
                print("No grades to display.")
                continue
            print("\nCurrent grades:")
            for sub, g in grades.items():
                print(f"  {sub}: {g}")
            avg = calculate_average(grades)
            print(f"\nAverage grade: {avg:.2f}")

        elif choice == "3":
            save_grades(grades)
            print(f"Grades saved to {FILENAME}")

        elif choice == "4":
            save_before_exit = input("Save before exit? (y/n): ").strip().lower()
            if save_before_exit == "y":
                save_grades(grades)
                print(f"Grades saved to {FILENAME}")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
