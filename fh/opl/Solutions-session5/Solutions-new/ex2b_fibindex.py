def index_of_fib(s):
    # The number 1 is the value of fib_1 and fib_2 so we choose to return fib_1
    if s == 1:
        return 1
    s1 = 1
    s2 = 1
    s3 = s1 + s2
    n = 3
    # Same calculation as in ex2a but now we keep calculating new fib values until we reach our limit s
    while s3 < s:
        s1 = s2
        s2 = s3
        s3 = s1 + s2
        # Increment the index of the calculated fib numer
        n += 1
    # If the limit was reached and it was a fib number (because s3 is one) then we have the index
    if s3 == s:
        return n
    return -1


def main():
    s = int(input("Enter a Fibonacci number: "))
    print("%d th number of Fibonacci is %d" % (index_of_fib(s), s))


main()
