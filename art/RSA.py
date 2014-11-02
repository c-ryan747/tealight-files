from random import randint
import math
from fractions import gcd

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# Two random 
p = 53
q = 59

n = p*q
print "n = " + str(n)

phin = ( q - 1 )*( p - 1 )
print "phi(n) = " + str(phin)

foundE = False
while not foundE:
  e = randint(2,phin-1)
  if gcd(e,phin) == 1:
    foundE = True
print "e = " + str(e)

d = (2*phin + 1)/e
print "d = " + str(d)
    
data = 89

c = (data**e)%n
print "c = " + str(c)

decrypted = (c**d)%n
print "decrypted = " + str(decrypted)

if data == decrypted:
  print "Success"