from tealight.art import (color, line)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

  
def drawBezier(points,n):
  color("black")
  lastDrawn = points[0]

  for i in xrange(1,int(n+1)):
    k = i*(100.0/n)
    tempPoints = points
    print points
    while len(tempPoints) > 1:
      for j in range(0,len(tempPoints)-2):
        tempPoints[j] = partWayBetween(tempPoints[j],tempPoints[j+1],k)
      tempPoints.pop()
    line(lastDrawn[0],lastDrawn[1],tempPoints[0][0],tempPoints[0][1])
    lastDrawn = tempPoints[0]
  
drawBezier([(50,300),(250,300),(100,200),(200,150)],10.0)
#drawBezier([(300,300),(350,200),(500,300),(450,150)],100.0)
#drawBezier([(550,250),(550,100),(750,250),(750,400)],100.0)