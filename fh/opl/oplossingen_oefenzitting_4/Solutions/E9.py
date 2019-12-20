num_1 = int(input())
num_2 = int(input())

# PRE: num_1 and num_2 are strictly positive natural numbers

lcm = num_1 * num_2
i = 1

# INV:  i <= lcm
#       and lcm is a common multiple of num_1 and num_2 (lcm % num_1 == 0 and lcm % num_2 == 0)
#       and for all natural numbers j, for which 0 < j < i, j is not a common multiple of num_1 and num_2

# After initialization:
#       i <= lcm since lcm is a common multiple of both num_1 and num_2, which are both strictly positive
#       and
#       lcm is a common multiple indeed
#       and there are no natural numbers for j, such that 0 < j < i
#  So: OK!

while (i < lcm):
    # INV and loop condtion, so:
    #       i < lcm
    #       and lcm is a common multiple of num_1 and num_2 (lcm % num_1 == 0 and lcm % num_2 == 0)
    #       and for all natural numbers j, for which 0 < j < i, j is not a common multiple of num_1 and num_2

    if (i % num_1 == 0 and i % num_2 == 0):
        lcm = i
    #       If this condition is True
    #               ==> i is a common multiple of both numbers,
    #                   and there are no smaller common multiples (from invariant)
    #                   and
    #                   now i == lcm
    #               ==> for all natural numbers j, for which 0 < j < i, j is not a common multiple of num_1 and num_2
    #               ==> INVARIANT HOLDS
    else:
        i += 1
    #       If the if-condition was False
    #               ==> i is not common multiple of both numbers
    #                   so, lcm is still a common multiple
    #                   and
    #                   for all natural numbers j, for which 0 < j < i, j is not a common multiple of num_1 and num_2
    #               ==> INVARIANT HOLDS

    # Since in both cases, the invariant holds, we have proven that the invariant is maintained in eacht iteration.

# TERMINATION when i >= lcm
#   So:
#       i == lcm
#       lcm is a common multiple
#       for all natural numbers j, for which 0 < j < lcm, j is not a common multiple of num_1 and num_2
#   So:
#       lcm is the smallest common multiple
#       ==> POST CONDITION

# FINITENESS:
# - VARIANT: lcm - i
# - LOWER BOUND: lcm is at most equal to num_1 * num_2 and i is at most equal to lcm + 1,
#       which gives us a lower bound of -1.
# - MONOTONIC DECREASE:
#           if the if-condition does not hold: i is increased by exactly 1, hence 'lcm - i' decreases
#           if the if-condition holds, lcm is decreased, since before the if-statement, i < lcm,
#              so by the assignment "lcm = i", lcm decreases, hence the variant decreases
#       This means that every iteration, the variant decreases by at least 1.
# - FINITE NUMBER OF DECREMENTS: since the variant decreases
#   monotonically by at least one at each iteration and both `num_1` and `num_2` are
#   constant, the lower bound will be reached at which point the loop ends.

# POST: lcm is the least common multiple of num_1 and num_2

print("The least common multiple of " + str(num_1) + " and " + str(num_2) + " is " + str(lcm))