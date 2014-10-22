from tealight.art import (color, line, spot, circle, box, image, text, background)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

def drawSpot(point):
  spot(point[0], point[1], 3)

pointA = (300,500)
pointB = (500,300)

controlA = (200,400)
controlB = (500,200)

color("red")
line(pointA[0],pointA[1],pointB[0],pointB[1])

line(pointA[0],pointA[1],controlA[0],controlA[1])
line(pointB[0],pointB[1],controlB[0],controlB[1])

color("black")

for i in xrange(1,50):
  pointAC = partWayBetween(pointA, controlA, i)
  pointCB = partWayBetween(controlB, pointB, i)
  pointCC = partWayBetween(controlA, controlB, i)
  
  drawSpot(pointAC)
  drawSpot(pointCB)
  drawSpot(pointCC)
  
  pointACCC = partWayBetween(pointAC, pointCC, i)
  drawSpot(pointACCC)