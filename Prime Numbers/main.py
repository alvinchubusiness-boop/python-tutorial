n = int(input("Please Enter a number: "))

if n < 2:
    # No primes to print
    print("There are no prime numbers less than or equal to", n)
    pass
else:
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    for num in range(2, n + 1):
        if is_prime[num]:
            print(num)