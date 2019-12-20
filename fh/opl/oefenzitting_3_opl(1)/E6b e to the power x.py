THRESHOLD = 0.01

x = int(input('Enter a number: '))

result = 0
n = 0

#initialise such that we enter the while loop
term = THRESHOLD + 1
while term > THRESHOLD:
    #calculate n!
    fac = 1
    for n in range(2, n + 1):
        # see the proof in exercise 6a
        fac *= n

    term = pow(x, n) / fac
    result += term
    n += 1

print('e^' + str(x) + " = " + str(result))
