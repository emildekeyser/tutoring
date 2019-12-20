number = int(input('Enter a number: '))

for n in range(1, number+1):
    is_prime = True
    i = 2
    while i < n and is_prime:
        if n % i == 0:
            is_prime = False
        else:
            i += 1

    if is_prime:
        print(n)
