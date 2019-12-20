from math import sqrt

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))

discriminant = pow(b, 2) - (4 * a * c)

if discriminant > 0:
    sol1 = (-b + sqrt(discriminant)) / (2 * a)
    sol2 = (-b - sqrt(discriminant)) / (2 * a)
    print("Has solution: YES")
    print("Solution 1:", sol1)
    print("Solution 2:", sol2)
elif discriminant == 0:
    sol1 = (-1 * b) / (2 * a)
    print("Has solution: YES")
    print("Solution 1:", sol1)
else:
    print("Has solution: NO")
