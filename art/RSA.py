from random import randint
import math

# Two random 
P = 53
q = 59

n = p*q
phin = (q-1)(p-1)

foundE = False
while not foundE:
  e = randint(2,phin-1)
  if n%e != 0:
    foundE = True

d = (2*phin + 1)/e    
    
data = 89
c = math.pow(data,e)%n

decrypted = math.pow(c,d)%n

if decrypted == data:
  print "Success"