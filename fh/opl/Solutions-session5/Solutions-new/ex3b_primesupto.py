from math import sqrt


def is_prime(n):
    # Edge case
    if n == 1:
        return False
    # Edge case
    elif n == 2:
        return True
    else:
        # You only need to check for division until sqrt(n) because: if n is not prime => n = a * b and if a = sqrt(n)
        # then b = sqrt(n). If this is not the case then a or b is smaller than sqrt(n) and therefor our upper bound is
        # sqrt(n)

        # Writing the for-loop as: 'for x in range(2,n)' is also correct but a lot less efficient
        # The round function rounds the float from sqrt(n) up to the nearest integer
        for x in range(2, round(sqrt(n))):
            if n % x == 0:
                return False
        return True


def primes_up_to(n):
    for i in range(2,n):
        if is_prime(i):
            # Print consecutive i's on the same line
            print(i, end="\t")


def main():
    n = int(input("Enter a number: "))
    print("All prime numbers up to %d are : " % n)
    primes_up_to(n)


main()
