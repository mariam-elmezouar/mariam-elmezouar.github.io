import math

n = int(input("Give me a number: "))

if n == 1:
    print("1 is not prime.")
elif n == 2:
    print(f"{n} is prime.")
else:
    is_prime = True
    i = 2
    while i <= math.isqrt(n) and is_prime:
        if n % i == 0:
            print(f"{n} is divisible by {i}.")
            is_prime = False
        else:
            i += 1

if is_prime:
    print(f"{n} is prime.")