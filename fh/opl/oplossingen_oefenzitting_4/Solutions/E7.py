import random

lst = random.sample(range(1, 20), 10)

# PRE: `lst` is a list of integers of size N > 0

i = 1
max_value = lst[0]

# INVARIANT: `max_value` == max({lst_0, lst_1, ..., lst_i-1}), i <= len(lst)
# INITIALIZATION: `i` == 1 and `max_value` == lst[0] => OK

while i < len(lst):
    # INVARIANT - `max_value` == max({lst_0, lst_1, ..., lst_i-1}), i <= len(lst)
    # AND
    # i < len(lst)
    if lst[i] > max_value:
        max_value = lst[i]
    # So
    #   `max_value` == max({lst_0, lst_1, ..., lst_i}), i < len(lst)
    i += 1
    # So
    #   `max_value` == max({lst_0, lst_1, ..., lst_i-1}), i <= len(lst)
    # So:
    #   Invariant is maintained

# TERMINATION:
#   when i >= len(lst) the loop terminates...
#   So, i == len (lst) (since the invariant also holds and indicates that i <= len(lst0) )
#   So, max_value == max({lst_0, lst_1, ..., lst_(len(lst)-1)}) which is the maximum value in lst => POST CONDITION

    # FINITENESS:
    # - VARIANT: N - `i`
    # - LOWER BOUND: `i` is at most equal to
    #   N due to the loop condition, at that point the variant is
    #   equal to 0: the lower bound of the variant
    # - MONOTONIC DECREASE: at each iteration, `i` is increased by exactly 1
    #   and the length of lst is constant.
    #   Therefore, the variant N - `i` decreases by exactly one.
    # - FINITE NUMBER OF DECREMENTS: since the variant decreases
    #   monotonically by one at each iteration and N is constant,
    #   the lower bound will be reached at which point the loop ends.

# POST: `max_value` == the maximum value in `lst`

print(str(max_value) + " is the largest value in list " + str(lst))