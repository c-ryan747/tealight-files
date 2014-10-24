from tealight.art import (color, line)

def partWayBetween(a,b,i):
  return (a[0] + (i*(b[0]-a[0])/100),a[1] + (i*(b[1]-a[1])/100))

  
def drawBezier(points,n,drawControl):
  if drawControl:
    color("red")
    lastDrawn = points[0]
    
    for i in xrange(0,len(points)):
      line(lastDrawn[0],lastDrawn[1],points[i][0],points[i][1])
      lastDrawn = points[i]
    
  color("black")
  lastDrawn = points[0]
  
  for i in xrange(1,int(n+1)):
    k = i*(100.0/n)
    tempPoints = list(points)
    
    while len(tempPoints) > 1:
      for j in xrange(0,len(tempPoints)-1):
        tempPoints[j] = partWayBetween(tempPoints[j],tempPoints[j+1],k)
      
      tempPoints.pop()
   
    line(lastDrawn[0],lastDrawn[1],tempPoints[0][0],tempPoints[0][1])
    lastDrawn = tempPoints[0]
  
drawBezier([(50,300),(50,500),(200,100),(200,300)],100.0,False)
drawBezier([(200,300),(200,50),(200,50),(50,300)],100.0,False)
#drawBezier([(400,300),(800,200),(100,200),(600,300)],1000.0)