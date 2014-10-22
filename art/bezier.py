from tealight.art import (color, line, spot, circle, box, image, text, background)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

def drawSpot(point):
  spot(point[0], point[1], 3)

pointA = (300,300)
pointB = (500,300)

controlA = (350,200)
controlB = (450,150)

color("red")
#line(pointA[0],pointA[1],pointB[0],pointB[1])

line(pointA[0],pointA[1],controlA[0],controlA[1])
line(pointB[0],pointB[1],controlB[0],controlB[1])

color("black")
lastDrawn = pointA
n = 1000

for i in xrange(1,n+1):
  k = i*(100/n)
  print 100/n
  pointAC = partWayBetween(pointA, controlA, k)
  pointCB = partWayBetween(controlB, pointB, k)
  pointCC = partWayBetween(controlA, controlB, k)
  
  #drawSpot(pointAC)
  #drawSpot(pointCB)
  #drawSpot(pointCC)
  
  pointACCC = partWayBetween(pointAC, pointCC, k)
  pointCCCB = partWayBetween(pointCC, pointCB, k)
  #drawSpot(pointACCC)
  #drawSpot(pointCCCB)
  
  pointFinal = partWayBetween(pointACCC, pointCCCB, k)
  line(lastDrawn[0],lastDrawn[1],pointFinal[0],pointFinal[1])
  lastDrawn = pointFinal
  