from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
    
def shape(side,edges):
  for i in xrange(0,edges):
    move(side)
    turn(360/edges)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    shape(decoration, 3)
    turn(angle)

turn(-90)
waterwheel(12,75)