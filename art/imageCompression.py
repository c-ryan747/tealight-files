from tealight.art import (color, box)

def drawGrid(x,y,n,s):
  for i in xrange(0,n):
    for j in xrange(0,n):
      box(x + i*1.5*s,y + j*1.5*s,s,s)
      
drawGrid(50,50,16,10)