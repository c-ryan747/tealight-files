from tealight.art import (color, image, line, spot, circle, box, image, text, background)
from tealight.utils import sleep
from math import sin, cos, pi

#background ("track.png")

  
class car:
  "Race car class"
  def __init__(self,x,y,angle):
    self.draw(x,y,angle,"black")
    
  def draw(self,x,y,angle,colour):
    angle = -angle
    
    self.points = [x-100*sin(angle),
                   y-100*cos(angle),
                   x-100*sin(angle+(2*pi/3)),
                   y-100*cos(angle+(2*pi/3)),
                   x-100*sin(angle+(4*pi/3)),
                   y-100*cos(angle+(4*pi/3))]
    self.x = x
    self.y = y
    self.angle = angle
    
    color(colour)
    
    line(self.points[0],self.points[1],self.points[2],self.points[3])
    line(self.points[2],self.points[3],self.points[4],self.points[5])
    line(self.points[4],self.points[5],self.points[0],self.points[1])
  
  def move(self,x,y,angle):
    self.draw(self.x,self.y,self.angle,"white")
    self.draw(x,y,angle,"black")
    
  

player1 = car(200,200,0)
#player1.move(200,200,pi/2)