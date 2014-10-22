from tealight.art import (color, line, spot, circle, box, image, text, background)

pointA = (300,500)
pointB = (500,300)

controlA = (200,400)
controlB = (600,200)

color("red")
line(pointA[0],pointA[1],pointB[0],pointB[1])

line(pointA[0],pointA[1],controlA[0],controlA[1])