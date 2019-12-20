import math

number = int(input('Enter a number: '))

# PRE: number is a strictly positive natural number

# We calculate how many digits in number (which will be called n in the proof below)
number_of_digits = math.floor(math.log (number, 10) + 1)

i = number_of_digits
reversed_number = 0

# INVARIANT:  number = the first i digits of the original number
#             AND
#             reversed_number = the last n-i digits of the original number in reverse order
#             (so in fact, the original number =  a textual version of number, concatenated with
#                       a textual version of the reverse of reversed_number)
#             AND
#             0 <= i <= number_of_digits

# INVARIANT holds after INITIALISATION?
#   i = number_of_digits
#   So:
#       number is the number with all digits of the original number
#       and
#       reversed number = the value of an empty list of digits, hence 0
#       and
#       and 0 <= number_of_digits <= number_of_digits
#   So:
#       indeed, invariant holds

while i != 0:
    # INVARIANT:
    #             number = the first i digits of the original number
    #             AND
    #             reversed_number = the last n-i digits of the original number in reverse order
    #             (so in fact, the original number =  a textual version of number, concatenated with
    #                       a textual version of the reverse of reversed_number)
    #             AND
    #             0 <= i <= number_of_digits
    # AND
    #    i != 0
    # So:
    #   0 < i <= number_of_digits
    reversed_number = reversed_number * 10 + number % 10
    # So now, reversed_number = the last n-(i+1) digits of the original number in reverse order, since the last digit
    # of number is just added to the reversed number after being shifted by 1 position
    number //= 10
    # This removes the last digit from number, leaving it with only the first (i-1) digits of the original number.
    # So:
    #     number = the first i-1 digits of the original number
    #     AND
    #     reversed_number = the last n-(i-1) digits of the original number in reverse order
    #     (so in fact, the original number =  a textual version of number, concatenated with
    #          a textual version of the reverse of reversed_number)
    #     AND
    #     0 <= i < number_of_digits
    i = i - 1
    # So:
    #     number = the first i digits of the original number
    #     AND
    #     reversed_number = the last n-i digits of the original number in reverse order
    #     (so in fact, the original number =  a textual version of number, concatenated with
    #          a textual version of the reverse of reversed_number)
    #     AND
    #     0 <= i <= number_of_digits
    # So:
    #     INVARIANT is maintained

# TERMINATION:
#   while loop ends when when i == 0
#   So, since the invariant is proven to hold, we have:
#             reversed_number = the last n digits of the original number in reverse order
# ==> POSTCONDITION holds


    # FINITENESS:
    # - VARIANT: `i`
    # - LOWER BOUND of `i` is equal to 0
    # - MONOTONIC DECREASE: at each iteration, `i` is integer divided by 10
    # - FINITE NUMBER OF DECREMENTS: since the variant decreases
    #   monotonically, and 0 <= i <= number_of_digits,
    #   the lower bound will be reached at which point the loop ends.

# POST:
#   reversed_number = the last n digits of the original number in reverse order

print(reversed_number)