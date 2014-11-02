from tealight.art import (color, box)

def drawGrid(x,y,n,s):
  for i in xrange(0,n):
    for j in xrange(0,n):
      box(i*1.5*s,j*1.5*s,s,s)
      
drawGrid(100,100,16,20)