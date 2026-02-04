while True:
    try:
        first_number = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        second_number = float(input("Enter the second number: "))
        if second_number == 0:
            print("Second number cannot be 0 (division by zero). Please enter another number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

sum = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print(sum)
print(subtraction)
print(multiplication)
print(division)