def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    num = int(input("Please enter a number: "))
    result = fibonacci(num)
    print("Fibonacci of", num, "is:", result)
    return result

main()