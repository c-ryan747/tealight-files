from tealight.art import (color, line, spot, circle, box, image, text, background)

pointA = (300,500)
pointB = (500,300)

controlA = (200,400)
controlB = (500,200)

color("red")
line(pointA[0],pointA[1],pointB[0],pointB[1])

line(pointA[0],pointA[1],controlA[0],controlA[1])
line(pointB[0],pointB[1],controlB[0],controlB[1])

colour("black")

for i in xrange(1,100):
  pointAC = (pointA[0] + (i*(controlA[0]-pointA[0])/100,pointA[1] + (i*(controlA[1]-pointA[1])/100)
  pointBC = (controlB[0] + (i*(pointB[0]-controlB[0])/100,controlB[1] + (i*(pointB[1]-controlB[1])/100)
  