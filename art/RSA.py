from random import randint
import math

# Two random 
p = 53
q = 59

n = p*q
print "n = " + str(n)
phin = ( q - 1 )*( p - 1 )

#foundE = False
#while not foundE:
#  e = randint(2,phin-1)
#  if n%e != 0:
#    foundE = True
e = 3

d = (2*phin + 1)/e    
    
data = 89
c = math.pow(data,e)%n

decrypted = math.pow(c,d)%n

