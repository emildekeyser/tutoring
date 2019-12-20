# plus is a variable that keeps track of whether the next
# operation has to be a plus or a minus
# plus == True --> the next operation has to be +
# plus == False --> the next operation has to be -
plus = True

n = int(input('Enter an integer number (enter 0 to stop): '))

sum = 0
while n != 0:
    if plus:
        sum += n
        plus = False
    else:
        sum -= n
        plus = True
    n = int(input('Enter an integer number (enter 0 to stop): '))

print('The alternating sum is', sum)
