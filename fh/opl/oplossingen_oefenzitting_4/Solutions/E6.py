import random

num = int(input())

lst = random.sample(range(1, 20), 10)

# PRE: `num` is an integer, `lst` is a list of integers of size N > 0

i = 0
num_found = False
# INVARIANT: i <= len(lst), `num_found` == False if `num` not in {lst_0, lst_1, ..., lst_i-1}, otherwise `num_found` == True
# AFTER INITIALIZATION: `i` == 0 and `num_found` == False, `num` not in {} (empty list) => OK

while i < len(lst):
    # INVARIANT: i <= len(lst), `num_found` == False if `num` not in {lst_0, lst_1, ..., lst_i-1}, otherwise `num_found` == True
    # AND
    # i < len(lst)
    if lst[i] == num:
        num_found = True
    # So:
    # i < len(lst), `num_found` == False if `num` not in {lst_0, lst_1, ..., lst_i}, otherwise `num_found` == True
    i += 1
    # i <= len(lst), `num_found` == False if `num` not in {lst_0, lst_1, ..., lst_i-1}, otherwise `num_found` == True
    # So:
    #   INVARIANT is maintained

# After TERMINATION:
#   INVARIANT holds
#   AND
#   i >= len(lst)
#   So:
#   `num_found` == False if `num` not in {lst_0, lst_1, ..., lst_(len(lst)-1}, otherwise `num_found` == True
#   => POST CONDITION


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

# POST: `num_found` == True if `num` ∈ `lst`, otherwise `num_found` == False

if (num_found): print("Number " + str(num) + " was found in list " + str(lst))
else: print("Number " + str(num) + " was not found in list " + str(lst))