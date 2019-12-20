def sum_up_to(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def main():
    n = int(input("enter a positive integer: "))
    print("The sum of the numbers from 1 to %d is %d" % (n, sum_up_to(n)))


main()
