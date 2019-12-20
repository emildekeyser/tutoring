def fac(n):
    fac = 1
    for i in range(1, 1+n):
        fac = fac * i
    return fac


def permutation(n, k):
    return fac(n)/fac(n-k)


def combination(n,k):
    return permutation(n, k)/permutation(k, k)


def main():
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    print("The number of combination is %d" % combination(n, k))


main()