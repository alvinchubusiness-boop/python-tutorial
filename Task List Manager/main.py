FILE_NAME = "tasks.txt"


def load_tasks(file_name=FILE_NAME):
    """Load tasks from a text file (one task per line)."""
    tasks = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        tasks = []
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except OSError as e:
        print(f"Error: Could not read file. ({e})")
    return tasks


def save_tasks(tasks, file_name=FILE_NAME):
    """Save tasks to a text file (one task per line)."""
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
    except PermissionError:
        print("Error: Permission denied while writing the file.")
    except OSError as e:
        print(f"Error: Could not write file. ({e})")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        idx = int(input("Enter the task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def view_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
        return
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def main():
    tasks = load_tasks()

    while True:
        print("=== Task List Manager ===")
        print("1) Add task")
        print("2) Remove task")
        print("3) View tasks")
        print("4) Save & Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Bye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
main()
