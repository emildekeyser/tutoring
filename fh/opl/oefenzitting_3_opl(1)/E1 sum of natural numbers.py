#version 1 using a while loop
n = int(input('Enter the number of terms: '))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('The sum of the first', n, 'natural numbers is', sum)

#version 2 using a for loop
n = int(input('Enter the number of terms: '))
sum = 0
# the for loop ranges from 1 to n+1 because the end of the range is exclusive
for term in range(1, n+1):
    sum += term
print('The sum of the first', n, 'natural numbers is', sum)