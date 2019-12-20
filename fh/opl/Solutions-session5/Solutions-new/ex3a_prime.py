# Import the square root function
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
        for x in range(2, round(sqrt(n)+1)):
            if n % x == 0:
                return False
        return True


def main():
    n = int(input("Enter a number: "))
    print(is_prime(n))


main()
