import random

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def main():
    # Generate a random list of 10 numbers between 1 and 100
    numbers = [random.randint(1, 100) for _ in range(10)]

    print("Random list of numbers:", numbers)

    average = calculate_average(numbers)
    print("The sum of the numbers is:", sum(numbers))
    print("The average is:", average)

    return average


main()
