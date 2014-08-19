from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in xrange(0, edges):
    move(size)
    turn(angle)
    
polygon(6,150) #hexagon

polygon(360,150/(360/6)) #crude circle