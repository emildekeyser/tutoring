def bubble_sort(input_list):
    for b in range(len(input_list)):

        for i in range(0, len(input_list) - b - 1):
            # 1. input_list[i] == max(input_list_before_inner[:i+1])
            #    and input_list is a permutation of input_list_before_inner
            if input_list[i] > input_list[i + 1]:
                # 2. input_list[i] > input_list[i+1]
                tmp = input_list[i]
                input_list[i] = input_list[i + 1]
                # 3. input_list_new[i] = input_list[i+1]
                input_list[i + 1] = tmp
            # 4. input_list_new[i+1] = input_list[i]
            # 5. input_list_new[i] <= input_list_new[i+1] and input_list_new is equal to the input_list except the elements at i and i + 1 which are swapped
            # 	this is true if we have entered the if-body (see above)
            #   this is true when we don't enter the if-body as then holds that input_list[i] > input_list[i+1] is false and input_list=input_list_new
            # from 1. and 2. follows input_list_new[i+1] == max(input_list_before_inner[:i+2]) and input_list_new is a permutation of input_list_before_inner
            # 6. i_new = i + 1 <=> i = i_new - 1
            # 7. input_list_new[i_new - 1 +1] == max(input_list_before_inner[:i_new - 1 +2]) and input_list_new is a permutation of input_list_before_inner
            #   so we proved that the inner invariant holds at the end of the loop, for the new value of i

    return input_list

# some notation:
#   - with input_list_start we denote input_list in the state it was in the beginning of the function.
#   - with permutation(l1, l2) we denote that a list l1 is a permutation of a list l2
#     (i.e., the contain the same elements, possibly in a different order)

# PRE: input_list is a list with elements on which an order is defined (<,>,=, are defined on the elements)

# POST: (1) input_list = sorted(input_list_start)
#       (2) permutation(input_list, input_list_start)

# STOP: (what should be true before you exit the for-loop):  b = len(input_list)

# INV: choose an INV such that (1) you can prove its existence (hint: first try to understand the code, so you can get an intuition for what expressions are true)
#                              (2) if STOP and INV hold, POST also holds
# INV = input_list[len(input_list)-b:] = sorted(input_list_start)[len(input_list)-b:] and permutation(input_list, input_list_start)
# Proof that POST + INV reduces to the POST condition:
#   from the STOP we know that we can substitute b by len(input_list) in the INV. This gives:
#   input_list[len(input_list)-len(input_list:] = sorted(input_list_start)[len(input_list)-len(input_list):] and permutation(input_list, input_list_start)
#   which is equal to POST

# Now we have shown that INV + STOP = POST, we need to prove that INV in fact holds for our program  and that the STOP condition becomes true at some point (=EINDIGHEID)

# Proof that INV holds:
# INV holds after initialization:
# if b = 0 then the invariant is trivially true:
#     input_list[len(input_list)-0:] = sorted(input_list_start)[len(input_list)-0:] <=> [] = sorted([])
#     permutation(input_list, input_list_start) holds since the input_list = input_list_start

# If INV holds in the beginning of the loop then it also holds at the end of the loop:
# Formally:  given           INV-holds in begin: input_list[len(input_list)-b:] = sorted(input_list_start)[len(input_list)-b:] and permutation(input_list, input_list_start)
#            we prove that   INV-holds at end: input_list_new[len(input_list)-b_new:] = sorted(input_list_start)[len(input_list)-b_new:] and permutation(input_list_new, input_list_start)
# Proof:
# The inner loop permutes input_list such that bth last element is the maximum of the first len(input_list) - b elements of input_list (in the state before the inner-loop starts)
# More formally the post condition of the inner loop:
# POST-INNER: input_list_after_inner[len(input_list)-b-1] = max(input_list_before_inner[:len(input_list)-b]) and permutation(input_list_after_inner, input_list_before_inner)

# 1.From POST-INNER and INV-holds in begin follows: input_list_before_inner[len(input_list)-b-1:] = sorted(input_list_start)[len(input_list)-b-1:] and permutation(input_list_before_inner, input_list_start)
# 2. At the end of the loop b increases: b_new = b + 1 <=> b = b_new - 1
# 3. From substitution follows that the INV holds at the end: input_list_before_inner[len(input_list)-b_new:] = sorted(input_list_start)[len(input_list)-b_new:] and permutation(input_list_before_inner, input_list_start)

# What remains is to proof POST-INNER:
# STOP-INNER: i = len(input_list) - b - 1
# INV-INNER: input_list[i] = max(input_list_before_inner[:i+1]) and permutation(input_list, input_list_before_inner)
# Proof that INV-INNER + STOP-INNER reduce to POST-INNER is trivial (substituting i by len(input_list) - b - 1 yields POST-INNER
# Proof that INV-INNER holds:
# INV-INNER holds after initialization:
# if i = 0 then the invariant is trivially true:
#   input_list[0] == max(input_list_before_inner[:1])  since the input_list = input_list_before_inner
#   input_list is a permutation of the input_list_before_inner since the input_list = input_list_before_inner
#
# If INV-INNER holds in the begin of the loop then it also holds at the end of the loop:
# Formally:  given           input_list[i] = max(input_list_before_inner[:i+1]) and permutation(input_list, input_list_before_inner)
#            we proof that   input_list[i+1] = max(input_list_before_inner[:i+1]) and permutation(input_list, input_list_before_inner)
# This is proven in the comments between the code.

# EINDIGHEID (outer):
# Variant: len(input_list) - b
# Lower bound:
#       b, len(input_list) element of natural numbers
#       len(input_list) won't ever change
#       b <= len(input_list) because:
#           b <= len(input_list) after init
#           every iteration ( b<len(input_list) ) b is incremented by one
#       so: len(input_list) - b >= 0
# Monotonous?
#      b, len(input_list) element of natural numbers
#      b is incremented each iteration, len(input_list) is constant
#      => every iteration len(input_list) - b is decremented with one
# Finite amount of decrements
#      b, len(input_list) element of natural numbers
#      len(input_list) is constant AND len(input_list) - b >= 0
#      every iteration len(input_list)-b  decremented by one
#      so: every iteration can be ran a maximum of `len(input_list)` times, which is finite
#
# inner loop is analogous to the above explanation
