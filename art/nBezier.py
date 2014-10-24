from tealight.art import (color, line)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

  
def drawBezier(points,n):
  color("black")
  lastDrawn = points[0]

  for i in xrange(1,int(n+1)):
    k = i*(100.0/n)

    while len(points) > 1:
      for j in range(0,len(points)-2):
        points[j] = partWayBetween(points[j],points[j+1],k)
      points.pop()
    print points
    line(lastDrawn[0],lastDrawn[1],points[0][0],points[0][1])
    lastDrawn = points[0]
  
drawBezier([(50,300),(250,300),(100,200),(200,150)],1000.0)
drawBezier([(300,300),(350,200),(500,300),(450,150)],1000.0)
drawBezier([(550,250),(550,100),(750,250),(750,400)],1000.0)