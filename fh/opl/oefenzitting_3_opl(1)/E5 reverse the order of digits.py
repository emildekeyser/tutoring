#rem_number will be the remainder of the number that we still have to reverse
rem_number = int(input('Enter a number: '))

reversed_number = 0

#in each iteration the last digit from rem_number is added at to the end of reversed_number
while rem_number > 0:
    #extract the last digit from remaining number
    last_digit = rem_number % 10
    #the reversed number is
    # the current reversed number * 10 (to make a zero at the end)
    # + the last_digit
    reversed_number = reversed_number * 10 + last_digit
    #the remaining number is now remaining number without the last digit
    rem_number = rem_number // 10

print(reversed_number)
