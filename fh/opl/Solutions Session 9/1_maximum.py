# Time complexity.
# The loop executes n-1 times
# AT_min = 1, AT_max = n, AT_avg = n/2
# AV = n
# T = AT_avg + AV = n/2 + n = O(n)
def maximum(a):
    i = 0
    max = a[i]          # INV: max_old = max(a[0:i]) 
    while i < len(a):   
        if a[i] > max:
            max = a[i]  # if a[i] > max_old then max_new = a[i] else max = max_old, so max = max(a[0:i+1]) 
        i = i + 1       # i = i_old + 1, so max = max(a[0:i-1+1]) = max(a[0:i]) (= INV)
    return max          


# PRE: `a` is a non-empty list of numbers

# POST: max = max(a[0:len(a)]) (i.e. max is the maximum of all elements in `a`)
# STOP: i >= len(a)
# INV: choose an INV such that (1) you can prove its existence (hint: first try to understand the code, so you can get an intuition for what expressions are true)
#                              (2) if STOP and INV hold, POST also holds
# INV: max = max(a[0:i]) and i <= len(a)   (i.e. max is the maximum of all elements in `a` starting from index 0 up to, and including, index i-1)

# Proof that indeed INV + STOP = POST:
#       i <= len(a) (=part of INV) and i >= len(a) (=STOP) <=> i = len(a)
#       max = max(a[0:i]) (=part of INV) and i = len(a) <=> max = max(a[0:len(a)])


# Now we have shown that INV + STOP = POST, we need to prove that INV in fact holds for our program  and that the STOP condition becomes true at some point (=EINDIGHEID)

# Proof that INV holds:
# INV holds after initialization: a[0] = max(a[0:0])  (substitute i and max by their initial values and rely on PRE)
# If INV holds in the begin of the loop then it also holds at the end of the loop:
# Formally:  given           max_old = max(a[0:i_old])
#            we proof that   max_new = max(a[0:i_new]), with subscripts old/new stands for the value at beginning/end of the iteration resp.
# Proof:
# See comments in code


# Proof for `EINDIGHEID`:
# we proof that at some point i < len(a) is false:
# we know that after every iteration  i <= len(a) (part of INV), every iteration i gets larger and len(a) remains constant (no elements added/removed)
# => at some point i >= len(a)
