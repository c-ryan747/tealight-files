from tealight.art import (color, line, spot, circle, box, image, text, background)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

def drawSpot(point):
  spot(point[0], point[1], 3)

  
def drawBezier(pointA,controlA,pointB,controlB,n):
  color("red")

  line(pointA[0],pointA[1],controlA[0],controlA[1])
  line(pointB[0],pointB[1],controlB[0],controlB[1])

  color("black")
  lastDrawn = pointA

  for i in xrange(1,int(n+1)):
    k = i*(100.0/n)

    pointAC = partWayBetween(pointA, controlA, k)
    pointCB = partWayBetween(controlB, pointB, k)
    pointCC = partWayBetween(controlA, controlB, k)
  
    pointACCC = partWayBetween(pointAC, pointCC, k)
    pointCCCB = partWayBetween(pointCC, pointCB, k)
  
    pointFinal = partWayBetween(pointACCC, pointCCCB, k)
  
    line(lastDrawn[0],lastDrawn[1],pointFinal[0],pointFinal[1])
    lastDrawn = pointFinal
  
drawBezier((50,300),(250,300),(50,200),(200,150),1000.0)
drawBezier((300,500),(350,400),(500,500),(450,350),1000.0)
drawBezier((300,700),(300,550),(500,700),(500,850),1000.0)