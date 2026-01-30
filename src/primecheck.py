import math

def isprime(n):
    if not isinstance(n, int) or n < 2:
        return False

    sqrt_n = int(math.sqrt(n))

    i = 2
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += 1

    return True
