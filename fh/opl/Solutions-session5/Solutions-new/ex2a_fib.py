def fib(n):
    # fib_1 and fib_2 are both equal to 1
    if n <= 2:
        return 1
    s1 = 1
    s2 = 1
    s3 = s1 + s2
    # if a number higher than fib_3 is requested then calculate it iteratively in the for-loop
    for i in range(4, n+1):
        # fib_n = fib_(n-1) + fib_(n-2)
        s1 = s2
        s2 = s3
        s3 = s1 + s2
    return s3


def main():
    n = int(input("Enter n: "))
    print("%d th number of Fibonacci is %d" % (n,fib(n)))


main()