from tealight.art import (color, box)
from random import randint

color("white")
box(0,0,10000,10000)

def randomGridData(n):
  data = [[0 for x in xrange(n)] for x in xrange(n)] 
  for i in xrange(0,n):
    for j in xrange(0,n):
      data[i][j] = randint(0,1)
   
  return data 

def drawGrid(x,y,n,s,data):
  counter = 0
  for i in xrange(0,n):
    for j in xrange(0,n):
      if data[i][j] == 0:
        color("Black")
      else:
        color("white")
      box(x + i*1.5*s,y + j*1.5*s,s,s)
      counter += 1
      
def makeDataTree(data):
  n = len(data)
  if n == 1:
    return data
  else:
    for i in xrange(0,n/2):
      for j in xrange(0,n/2):
        return 0
        


Sample = randomGridData(16)
print len(Sample)
drawGrid(50,50,16,12,Sample)