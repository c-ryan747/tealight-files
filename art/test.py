from math import pi,sin,cos

amount = 5
angle = 0
radius = 100
cx = 1000
cy = 1000

print(pi/2)
for i in xrange(1,amount+2):
#  print(angle)
  
  x = cos(angle)*radius +cx
  y = sin(angle)*radius +cy
  print("x:",str(x),"y:",str(y))
  angle = angle + (pi/2)/amount