def factorial(n):
    if n < 0:
        return "Undefined. Factorial is not defined for negative numbers. Please try again with a non-negative integer."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    num = int(input("Please enter a number: "))
    result = factorial(num)
    print("Factorial of", num, "is:", result)
    return result

main()
