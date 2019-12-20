first = float(input("Enter a floating-point number: "))
second = float(input("Enter a second floating-point number: "))
if round(first, 2) == round(second, 2):
    print("They are the same up to two decimal places.")
else:
    print("They are different.")
