#The value 0 is given just to avoid syntax errors
x,y = 0

#What is the difference?

#1
s = 0
if x > 0:
    s = s + 1
if y > 0:
    s = s + 1

#2
s = 0
if x > 0:
    s = s + 1
elif y > 0:
    s = s + 1

'''
The difference is the elif statement instead of the if statement.
The elif statement is a combination of else and if, you can rewrite it like this:

s = 0
if x > 0:
    s = s + 1
else:
    if y > 0:
        s = s + 1


So the difference with the two is that if both x and y are higher as 0,
the first piece of code will increment S two times whereas in the second piece of code
S will only be incremented one time.

'''
