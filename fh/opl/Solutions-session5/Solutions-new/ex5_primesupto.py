import math


def fac(n):
    fac = 1
    for i in range(1, 1+n):
        fac = fac * i
    return fac


def estimate_exp(x, n):
    som = 0
    # Exactly the formula in the question written in code
    for i in range(0, n+1):
        term = math.pow(x, i)/fac(i)
        som += term
    return som


# delta is the minimum value of the calculated term
def estimate_exp2(x, delta):
    i = 0
    term = math.pow(x, i)/fac(i)
    som = term
    while term > delta:
        i += 1
        term = math.pow(x, i)/fac(i)
        som += term
    return som


def main():
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    print("e powered by %d is %f" % (x, estimate_exp(x, n)))
    delta = float(input("Enter delta: "))
    print("e powered by %d is %f" % (x, estimate_exp2(x, delta)))


main()