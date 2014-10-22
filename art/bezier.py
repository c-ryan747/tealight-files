from tealight.art import (color, line, spot, circle, box, image, text, background)

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
  pointAC = (pointA[0] + (i*(controlA[0]-pointA[0])/100),pointA[1] + (i*(controlA[1]-pointA[1])/100))
  pointBC = (controlB[0] + (i*(pointB[0]-controlB[0])/100),controlB[1] + (i*(pointB[1]-controlB[1])/100))
  pointCC = (controlA[0] + (i*(controlB[0]-controlA[0])/100),controlA[1] + (i*(controlB[1]-controlA[1])/100))
  spot(pointAC[0],pointAC[1],5)
  spot(pointBC[0],pointBC[1],5)
  spot(pointCC[0],pointCC[1],5)