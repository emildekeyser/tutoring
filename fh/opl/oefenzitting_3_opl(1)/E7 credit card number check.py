# if we want the last digit of the number 'n', we use:
# n % 10
# if we want to get the number 'n' without the last digit, we use:
# n // 10
# examples:
# 101 % 10 == 1
# 101 // 10 == 10

number = int(input('Enter 8-digit credit card number: '))

# step 1
first_step_result = 0
n1 = number
for i in range(0, 4):
    last_digit = n1 % 10
    first_step_result += last_digit
    n1 //= 100

# step 2
second_step_result = 0
n2 = number
n2 //= 10
for i in range(0, 4):
    last_digit_doubled = (n2 % 10)*2
    second_step_result += last_digit_doubled % 10 + last_digit_doubled // 10
    n2 //= 100

# step 3
if (first_step_result + second_step_result) % 10 == 0:
    print('The credit card number is valid')
else:
    print('The credit card number is not valid')
    valid_last_digit = (number - first_step_result - second_step_result) % 10
    print('The last digit should be',valid_last_digit)
