from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines, xstretch, ystretch):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    
    x0 = x + (size * cos(angle) * xstretch)
    y0 = y + (size * sin(angle) * ystretch)
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

star(300, 300, "blue", 100, 50,1.5,1)
star(600, 400, "purple", 100, 100,1,1.5)
