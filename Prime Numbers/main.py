n = int(input("Please Enter a number: "))
print("The list of prime numbers between 2 and a number given by user is:")
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
       