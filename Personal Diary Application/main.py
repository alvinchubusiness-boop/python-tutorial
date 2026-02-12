from datetime import datetime

DIARY_FILE = "diary.txt"


def add_entry(filename: str) -> None:
    entry = input("Write your diary entry:\n> ").strip()
    if not entry:
        print("Empty entry not saved.")
        return

    add_time = input("Add timestamp? (y/n): ").strip().lower()
    timestamp = ""
    if add_time == "y":
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(timestamp + entry + "\n")
            f.write("-" * 40 + "\n")
        print("File saved.")
    except PermissionError:
        print("Permission denied: cannot write to the diary file.")
    except OSError as e:
        print(f"File error while saving: {e}")


def view_entries(filename: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                print("No entries found yet.")
            else:
                print("\n📖 Your Diary Entries")
                print("=" * 40)
                print(content)
                print("=" * 40)
    except FileNotFoundError:
        print("No diary file found yet. Add an entry first to create it.")
    except PermissionError:
        print("Permission denied: cannot read the diary file.")
    except OSError as e:
        print(f"File error while reading: {e}")


def main():
    while True:
        print("\n=== Personal Diary Application ===")
        print("1) Add new entry")
        print("2) View previous entries")
        print("3) Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_entry(DIARY_FILE)
        elif choice == "2":
            view_entries(DIARY_FILE)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
