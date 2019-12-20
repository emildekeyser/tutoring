# assuming that `*` is a more expensive operation than `=` or `+`

def eval1(coef, x):
    res = 0.0
    for i in range(0,len(coef)):
        term = float(coef[i])
        for j in range(0,i):
            # this line will be executed i times
            # in every iteration of the outer loop,
            # so if n is the length of `coef`, then
            # T(n) = sum(0..n) = n*(n+1)/2 = O(n²)
            term = term * x 
        res = res + term
    return res

def eval2(coef, x):
    res = 0.0
    term = 1.0
    for i in coef:
        # 2 `*` operations will be executed for every
        # element in `coef`, so
        # T(n) = 2*n = O(n)
        res = res + term * i
        term = term * x
    return res

def eval3(coef, x):
    res = float(coef[-1])
    for i in range(len(coef)-2, -1, -1):
        # there is one `*` operation that gets
        # executed n-1 times, so
        # T(n) = n-1 = O(n)
        # even though `eval3` is more efficient than
        # `eval2`, they are both of the same order
        res = res * x + coef[i]
    return res
