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
    size =100

    self.points = [x-size*sin(angle),
                   y-size*cos(angle),
                   x-size*sin(angle+(2*pi/3)),
                   y-size*cos(angle+(2*pi/3)),
                   x-size*sin(angle+(4*pi/3)),
                   y-size*cos(angle+(4*pi/3))]
    
    self.draw_points(self.points,colour)
  
  def draw_points(self,points,colour):
    color(colour)
    line(points[0],points[1],points[2],points[3])
    line(points[2],points[3],points[4],points[5])
    line(points[4],points[5],points[0],points[1])
  
  def move(self,x,y,angle):
    self.draw_points(self.points,"white")
    self.draw(x,y,angle,"black")
    
  

player1 = car(200,200,0)
#player1.move(200,200,pi/2)