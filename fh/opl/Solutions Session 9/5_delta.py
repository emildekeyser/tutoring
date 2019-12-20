# Simply looking at the method with 2 loops. One may say the complexity is O(n²). 
# But looking at the method more closely, the code within the inner loop will be 
# invoked exactly n times at most, thus the complexity is O(n).
def containsdelta(lst, delta):
    j = 0
    for i in range(0, len(lst)):
        while (j < len(lst)-1) and (lst[i]-lst[j] > delta):
            j = j + 1
        if lst[i]-lst[j] == delta:
            return True
    return False

containsdelta([1,2,3,4,5,6,7,8,9,10],3)
