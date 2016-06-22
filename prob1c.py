import math
a = 3
b = 1
n=10
d = (a-b)/n
d = 
l = 1
r = 1

intgl = 0
intgr = 0
while l <= a-d:
    l = l + d
    functl = l ** math.log(l)
    intgl = intgl + (d * functl)
    functr = r ** math.log(r)
    intgr = intgr + (d * functr)
    r = r + d

print "L= ", intgl
print "R= ", intgr
print intgl - intgr < .01
