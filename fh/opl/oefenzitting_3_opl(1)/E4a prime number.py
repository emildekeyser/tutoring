number = int(input('Enter a number: '))

is_prime = True
i = 2

while i < number and is_prime:
    if number % i == 0:
        is_prime = False
    else:
        i += 1

if is_prime:
    print(number, 'is a prime number')
else:
    print(number, 'is not a prime number')
