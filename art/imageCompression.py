from tealight.art import (color, box)
from random import randint

def randomGrid(x,y,n,s):
  data = []
  for i in xrange(0,n*n):
    data.append(randint(0,1))
  print data
  drawGrid(x,y,n,s,data)

def drawGrid(x,y,n,s,data):
  counter = 0
  for i in xrange(0,n):
    for j in xrange(0,n):
      if data[counter] = 0:
        color("Black")
      else:
        color("white")
      box(x + i*1.5*s,y + j*1.5*s,s,s)
      counter++
      
      
randomGrid(50,50,16,10)