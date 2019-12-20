# Calculate the sum of all divisors of n
def sum_of_proper_divisors(n):
    s = 1
    for i in range(2, n):
        # Check if i divides n and if it does, add it to the sum s
        if n % i == 0:
            s += i
    return s


def is_perfect(n):
    return n == sum_of_proper_divisors(n)


def perfects_up_to(n):
    for i in range(2,n):
        if is_perfect(i):
            # Print consecutive i's on the same line
            print(i, end="\t")


def main():
    n = int(input("Enter a number: "))
    print("All perfect numbers up to %d are : " % n)
    perfects_up_to(n)


main()
