def ruler(n):
    if n == 1:
        print("-")
    else:
        print("-" * n)
        ruler(n - 1)
        print("-" * n)
        ruler(n - 1)
        print("-" * n)

def main():
    n = int(input("Enter a number: "))
    ruler(n)

main()
