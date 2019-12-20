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


def sum_of_fib(start,end):
    s = 0
    # Calculate all fib numbers starting from the starting number until 'end + 1' because a for-loop
    # stops with 'i = b - 1' as last value given: 'for i in range(a,b):'
    for i in range(start,end+1):
        s += fib(i)
    return s


def main():
    start = int(input("Enter start point: "))
    end = int(input("Enter end point: "))
    print("The sum of Fibonacci statements from %d to %d is %d" % (start, end, sum_of_fib(start,end)))


main()
