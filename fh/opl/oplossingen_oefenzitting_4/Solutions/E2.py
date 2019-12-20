num = int(input('Enter a number: '))

# PRE: num is a natural number

factorial = 1
i = 1

# INVARIANT: factorial = (i-1)! AND i <= num
# AFTER INITIALIZATION: i = 1, factorial = 1 = 0! => OK

while (i != num+1):
    # INVARIANT: factorial = (i-1)! AND i <= num
    # AND
    # i != num
    # SO:       factorial = (i-1)! AND i < num
    factorial *= i
    # factorial = i!  AND  i < num
    i += 1
    # factorial = (i-1)!  AND  i <= num
    # SO:   MAINTAINED!

# TERMINATION: when i == num + 1
# AND
# INVARIANT: factorial = (i-1)! = num! (POST CONDITION)

    # FINITENESS:
    # - VARIANT: `num` - `i`
    # - LOWER BOUND: `i` is at most equal to
    #   `num` + 1 due to the loop condition and increment, at that point the variant is
    #   equal to -1: the lower bound of the variant
    # - MONOTONIC DECREASE: at each iteration, `i` is increased by exactly 1.
    #   Therefore, the variant `num` - `i` decreases by exactly one.
    # - FINITE NUMBER OF DECREMENTS: since the variant decreases
    #   monotonically by one at each iteration and `num` is constant,
    #   the lower bound will be reached at which point the loop ends.

# POST: factorial = 1*2*3*...*num

print(str(num) + '! = ' + str(factorial))