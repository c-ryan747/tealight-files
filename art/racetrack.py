from tealight.art import (color, image, line, spot, circle, box, image, text, background)
from math import sin, cos, pi

#background ("track.png")

  
class car:
  "Race car class"
  def __init__(self):
    return
  def draw(self,x,y,angle):
    
    self.points = [x-100*sin(angle),
                   y-100*cos(angle),
                   x-100*sin(angle+(2*pi/3)),
                   y-100*cos(angle+(2*pi/3)),
                   x-100*sin(angle+(4*pi/3)),
                   y-100*cos(angle+(4*pi/3))]
    for i in range(0,2):
      line(self.points[0+2*i],self.points[1+2*i],self.points[2+2*i],self.points[3+2*i])

  

player1 = car()
player1.draw(200,200,pi/2)