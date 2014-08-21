  def circle_points(amount, radius,cx,cy,corner,array):
    angle = 0
    for i in xrange(1,amount):
      x = sin(angle)*radius
      y = cos(angle)*radius
      if corner == 1:
        array.append((x+cx,y+cy))
      angle = angle + (pi/2)/i
      
angle = 0 
for i in xrange(1,amount):
  print(angle)
  angle = angle + (pi/2)/i