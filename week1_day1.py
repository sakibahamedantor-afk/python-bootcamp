# Week 1 Day 1: First Python Program

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print primes up to 100
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
