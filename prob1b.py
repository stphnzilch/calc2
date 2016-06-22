import math
def funct(x):
    return x ** math.log(x)
a = 1.00
b = 3
intg = 0.00
n = 100.000
deltan = (b-a)/n
x = a

while x < b:
   
    fx = funct(x)
    intg = intg + (deltan * fx)
    x = x + deltan
print "L(n)= ", intg

