#E1 a
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print("The factorial of " + str(n) + " is " + str(factorial(n)))

#E1 b
def power(x,n):
    if n <= 0:
        return 1
    return x * power(x,n-1)

x = int(input("Enter a base: "))
n = int(input("Enter the power: "))
print("The power of " + str(x) +  " to " + str(n) + " is " + str(power(x,n)))

#E1 c
#Method that uses recursion as well as iteration. See the enxt solution for one without any iteration.
def factors(x, last = 2):
    if x == 1:
        return []
    for i in range(last, int( x ** .5 ) + 1 ):
        if x % i == 0:
            return [i] + factors(int(x / i), i)
    return [x]
#Another way of implementation without an inner for-loop.
def factors2(x, acc = 2):
    if x < acc:
        return []
    if x % acc == 0:
        return [x] + factors2(x / acc, 2)
    return factors2(x, acc + 1)

n = int(input("Enter a number: "))
print("The factors of " + str(n) + " are " + str(factors(n)))
