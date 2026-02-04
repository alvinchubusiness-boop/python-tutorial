while True:
    try:
        start_year = int(input("Enter the start year (person born/item created): "))
        end_year = int(input("Enter the current year: "))

        if start_year < 0 or end_year < 0:
            print("Years cannot be negative. Try again.")
            continue

        if start_year > end_year:
            print("Start year cannot be greater than current year. Try again.")
            continue

        break  # ✅ inputs are valid, exit loop

    except ValueError:
        print("Invalid input. Please enter numbers only.")

age = end_year - start_year

print("The calculated age is:", age)