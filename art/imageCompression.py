from tealight.art import (color, box)

def drawGrid(n):
  for i in xrange(0,n):
    for j in xrange(0,n):
      box(i*3,j*3,2,2)
      
drawGrid(16)