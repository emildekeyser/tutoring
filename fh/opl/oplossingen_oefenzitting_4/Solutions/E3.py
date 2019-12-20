s = input()

# PRE: `s` is a string of characters in
#   {a, b, ..., z, A, B, ..., Z}
#       = {a, b, ..., z} U {A, B, ..., Z}
#       = LOWER U UPPER,
#   len(s) >= 0

len_string = len(s)
counter = 0
amt = 0

# INVARIANT:
#   1. `amt` is equal to the size of {s[0], s[1] ..., s[counter-1]} ∩ UPPER
#       (the number of uppercase characters seen so far)
#   AND
#   2.  counter <= len_string

# AFTER INITIALIZATION? at initialization
#   1. `len_string` == the number of characters in `s`
#       `counter` == 0 and `amt` == 0 == the size of {}, the empty set => OK
#   2. counter (which is 0)  <= len_string (which is always >= 0)

while counter < len_string:
    # INVARIANT
    # AND
    # counter < len_string
    # SO: 1. amt` is equal to the size of {s[0], s[1] ..., s[counter-1]} ∩ UPPER
    #     AND
    #     2.  counter < len_string
    if s[counter].isupper():
        amt += 1
    # SO: 1. amt` is equal to the size of {s[0], s[1] ..., s[counter]} ∩ UPPER
    #     AND
    #     2.  counter < len_string
    counter += 1
    # SO: 1. amt` is equal to the size of {s[0], s[1] ..., s[counter-1]} ∩ UPPER
    #     AND
    #     2.  counter <= len_string
    # SO: INVARIANT MAINTAINED


    # TERMINATION:
    #   the loop ends when `counter` >= `len_string`
    #   and the INVARIANT says that counter <= len_string
    #   So: counter == len_string
    #
    #   The INVARIANT also indicates that
    #   `amt` is equal to the size of {s_0, s_1, ..., s_{counter - 1}} ∩ UPPER
    #   so:
    #       `amt` is equal to the size of {s_0, s_1, ..., s_{len_string - 1}} ∩ UPPER
    #   => POST condition reached

    # FINITENESS:
    # - VARIANT: `len_string` - `counter`
    # - LOWER BOUND: `counter` is equal to at most `len_string`, at that point
    #   the variant is equal to 0
    # - MONOTONIC DECREASE: at each iteration, `counter` is increased by exactly 1
    #   so the variant decreases by exactly one
    # - FINITE NUMBER OF DECREMENTS: since the variant decreases
    #   monotonically by one at each iteration and `len_string` is constant,
    #   the lower bound will be reached at which point the loop ends.

# POST: `amt` contains the size of `s` ∩ UPPER
#   (the number of uppercase characters in the string)

print('\"' + s + '\" contains ' + str(amt) + ' uppercase characters.')