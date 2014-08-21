from math import pi,sin,cos

amount = 5
angle = 0
radius = 100

print(pi/2)
for i in xrange(1,amount+2):
  print(angle)
  
  x = sin(angle)*radius
  y = cos(angle)*radius
  print("x:",str(x),"y:",str(y))
  angle = angle + (pi/2)/amount