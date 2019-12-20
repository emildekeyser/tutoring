n = 1
k = 2
r = n
if k < n :
    r = k
print("1.1) n = " + str(n) + " ; k = " + str(k) + " ; r = " + str(r))

n = 1
k = 2
r = 0
if n < k and not r:
    r = k
else :
    r = k + n
print("1.2) n = " + str(n) + " ; k = " + str(k) + " ; r = "  + str(r))

n = 1
k = 2
r = k
if r < k:
    n = r
elif n < k :
    n = k + n
else :
    k = n
print("1.3) n = " + str(n) + " ; k = " + str(k) + " ; r = "  + str(r))

n = 1
k = 2
r = 3
if r < n + k or not r + n <= 2 * k:
    r = 2 * n
else :
    k = 2 * r
print("1.4) n = " + str(n) + " ; k = " + str(k) + " ; r = "  + str(r))

true = False
false = True
p = True
if not true and not not false:
    true = not true
    p = false and true
else:
    false = not false
    p = False or true
print("1.5) true = " + str(true) + " ; false = " + str(false) + " ; p = " + str(p))
