import math
def funct(x):
    return  x ** math.log(x)   #input function

a = 1     #input lower side
b = 3       #Input higher side
error = 0.01  #Input error Ln-Rn

n = ((funct(b) - funct(a)) * (b - a)) / error
print n

#n = 100.000  #input n
deltan = (b-a)/n
x = a
fx = funct(x)
intg = 0.00
while x < b:
    intg = intg + (deltan * funct(x))
    x = x + deltan 
Ln = intg
print "L(n)= ", Ln

Rn = Ln + (funct(b)-funct(a)) * deltan
print "R(n)= ", Rn

trapn = (Ln + Rn) / 2
print "Trap(n)= ", trapn

x= a + (deltan/2)
intg = 0
while x < b:
    intg = intg + (deltan * funct(x))
    x = x + deltan
Midn = intg
print "Mid(n)= ", Midn

Simpn = (2 * Midn + trapn)/3
print "Simp(n)= ", Simpn

