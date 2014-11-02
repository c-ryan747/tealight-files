from random import randint
import math

# Two random 
p = 53
q = 59

n = p*q
print "n = " + str(n)

phin = ( q - 1 )*( p - 1 )
print "phi(n) = " + str(phin)

#foundE = False
#while not foundE:
#  e = randint(2,phin-1)
#  if n%e != 0:
#    foundE = True
e = 3
print "e = " + str(e)

d = (2*phin + 1)/e
print "d = " + str(d)
    
data = 89

c = (data**e)%n
print "c = " + str(c)

decrypted = math.pow(c,d)%n
print "decrypted = " + str(decrypted)
