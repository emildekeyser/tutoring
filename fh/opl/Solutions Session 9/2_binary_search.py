# NOTE: `=>` stands for logical implication, `<=` / '>=' stand for less than or equal / greater than or equal resp.
import math

# Time complexity.
# At each iteration of the while loop, the number of elements
# in sortedlist[indexmin:indexmax] is half of that number
# in the previous iteration.
# The number of iterations of the while loop is therefore log_2(n).
# The number of comparisons and assignments inside the while loop
# is constant (say C).
# T = C*log_2(n) = O(log_2(n))
#
# Space complexity.
# S = 2 + n = O(n)
def binary_search(sortedlist, needle):
    indexmin = 0
    indexmax = len(sortedlist)-1
    while indexmin < indexmax:
        # 1. indexmin_old < indexmax_old (condition of while)
        indexmid = int(math.floor((indexmax + indexmin)/2.0))
        # 2. indexmin <= indexmid < indexmax (by definition of `floor` and 1.)
        if needle <= sortedlist[indexmid]:
            # 3. needle <= sortedlist[indexmid:] (condition if + PRE)
            indexmax = indexmid
            # 4. needle <= sortedlist[indexmax_new:]  (index_max_new = indexmid + 3.)
            # 5. in this branch indexmin_new = indexmin_old
            # 6. needle in sortedlist => sortedlist[0:indexmin_new] <= needle <= sortedlist[indexmax_new:] (because 4. and .5 and INV holds for indexmin_old and indexmax_old)
            # 7. indexmin_new <= indexmax_new  (1. + 2. + indexmax_new = indexmid + 5.)
            # 8. INV = 6. and 7. 
        else:
            # 9.  needle > sortedlist[:indexmid] (negation condition if + PRE)
            # 10. needle >= sortedlist[:indexmid+1] (9. + PRE) 
            indexmin = indexmid + 1
            # 11. needle <= sortedlist[indexmax_new:]  (asignment + 3.)
            # 12. in this branch  indexmax_new = indexmax_old
            # 13. needle in sortedlist => sortedlist[0:indexmin_new] <= needle <= sortedlist[indexmax_new:] (because 11. and 12. and INV holds for indexmin_old and indexmax_old)
            # 14. indexmin_new <= indexmax_new  (1. + 2. + (indexmin_new = indexmid + 1) + 12.)
            # 15. INV = 13. and 14.

        # INV holds here because it holds after all branches of the if (8. and 15.) Q.e.d.
    if needle == sortedlist[indexmax]:
        return indexmax
    else:
        return None


# PRE: `sortedlist` is a list that is sorted from low to high

# POST: needle in sortedlist => needle = sortedlist[indexmax] and indexmax = indexmin

# STOP (the negation of the while condition): indexmin >= indexmax

# INV: choose an INV such that (1) you can prove its existence (hint: first try to understand the code, so you can get an intuition for what expressions are true)
#                              (2) if STOP and INV hold, POST also holds
# INV = needle in sortedlist => sortedlist[0:indexmin] <= needle <= sortedlist[indexmax:]  and indexmin <= indexmax
#      
# Proof that (2) is indeed true:  indexmin <= indexmax (=part of INV) AND indexmin >= indexmax (=STOP) <=> indexmin = indexmax
#                                 sortedlist[0:indexmax] <= needle <= sortedlist[indexmax:] <=> needle = sortedlist[indexmax]  (we substituted indexmin with indexmax in INV)


# Now we have shown that INV + STOP = POST, we need to prove that INV in fact holds for our program  and that the STOP condition becomes true at some point (=EINDIGHEID)

# Proof that INV holds:
# INV holds after initialization: needle in sortedlist => sortedlist[0:0] <= needle <= sortedlist[len(sortedlist) -1:]  and 0 <= len(sortedlist) -1 (substitute indexmin and indexmax by their initial values)
# The above expression is trivially true for a sortedlist (which is our precondition (PRE))
# If INV holds in the begin of the loop then it also holds at the end of the loop:

# Formally:  given           needle in sortedlist => sortedlist[0:indexmin_old] <= needle <= sortedlist[indexmax_old:]  and indexmin_old <= indexmax_old, 
#            we proof that   needle in sortedlist => sortedlist[0:indexmin_new] <= needle <= sortedlist[indexmax_new:]  and indexmin_new <= indexmax_new
# Proof:
# See comments in code


# Proof for `EINDIGHEID`:
# we proof that at some point indexmin >= indexmax is true:
# we know that after every iteration indexmin <= indexmax (part of INV), and every iteration either indexmax smaller (see 2. and indexmax = indexmid) or indexmin gets larger (see 2. and indexmin = indexmid + 1)
# => at some point indexmin = indexmax

