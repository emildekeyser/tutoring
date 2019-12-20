# See solution without functions for explanation of the code


def intermediate_result(number):
    num_step1 = number
    result_step1 = 0
    for i in range(0, 4):
        result_step1 += num_step1 % 10
        num_step1 //= 100
    num_step2 = number
    result_step2 = 0
    num_step2 //= 10
    for i in range(0, 4):
        x = num_step2 % 10
        x1 = (x*2) % 10
        x2 = (x*2) // 10
        result_step2 += x1 + x2
        num_step2 //= 100
    return result_step1+result_step2


def is_valid(number):
    if intermediate_result(number) % 10 == 0:
        return True
    else:
        return False


def make_valid(number):
    return (number-intermediate_result(number)) % 10


def main():
    number = int(input('Enter 8-digit credit card number: '))
    if is_valid(number):
        print('The credit card number is valid')
    else:
        print('The credit card number is not valid')
        print('The last digit should be %i' % make_valid(number))

main()