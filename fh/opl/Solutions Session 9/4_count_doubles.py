def count_doubles(seq):
    result = 0
    for i in range(0, len(seq)):
        # INVARIANT: result contains the number of doubles that are found for seq for the values in interval [0, i[ of seq
        for j in range(i+1, len(seq)):
            # INVARIANT: the outer invariant holds and result also contains the number of doubles for the i-th item of seq in interval [i+1,j[
            if seq[i] == seq[j]:
                result += 1
    return result

assert count_doubles([]) == 0
assert count_doubles([1, 1]) == 1
assert count_doubles([1, 1, 1]) == 3
assert count_doubles([2, 2, 1, 2, 2]) == 6
assert count_doubles([4, 6, 3, 2, 4, 1, 8, 3, 8]) == 3


### Time complexity:
# The outer loop executes O(n) times
# The inner loop executes O(n) times
# Overall, the algorithm runs in O(n^2) time.


### When seq is sorted, the doubles can be found in linear time. Note that this is similar to the longest plateau exercises.
def count_doubles_sorted(seq):
    start = 0
    result = 0
    if len(seq) == 0:
        return 0
    for i in range(0, len(seq)):
        # INVARIANT result contains the total number of doubles in the interval [0, start[ of seq
        if seq[i] != seq[start]:
            # If we get to a different value, we use the number of occurrences of the previous value to determine the number of doubles.
            # This is calculated as n*(n-1)/2 with n the number of occurrences of the value
            nb_occ = i - start
            result += nb_occ * (nb_occ - 1) / 2
            start = i
    return result + ((len(seq) - start) * (len(seq) - start - 1) / 2)

assert count_doubles_sorted([]) == 0
assert count_doubles_sorted([1, 1]) == 1
assert count_doubles_sorted([1, 1, 1]) == 3
assert count_doubles_sorted([1, 2, 2, 2, 2]) == 6
assert count_doubles_sorted([1, 2, 3, 3, 4, 4, 6, 8, 8]) == 3


### Time complexity:
# The only loop executes O(n) times, hence the overall algorithm has time complexity O(n)
