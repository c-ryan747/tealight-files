from tealight.art import (color, screen_width, screen_height, image, line, spot, circle, box, image, text, background)
from tealight.utils import sleep
from math import sin, cos, pi

#background ("track.png")

  
class car:
  "Race car class"
  
  def __init__(self,x,y,angle):
    self.draw(x,y,angle,"black")
    
  def draw(self,x,y,angle,colour):
    size = 40

    self.points = [x+size*cos(angle),
                   y-size*sin(angle),
                   x+(size/2)*cos(angle+(2*pi/3)),
                   y-(size/2)*sin(angle+(2*pi/3)),
                   x+(size/2)*cos(angle+(4*pi/3)),
                   y-(size/2)*sin(angle+(4*pi/3))]
    
    self.draw_points(self.points,colour)
  
  def draw_points(self,points,colour):
    color(colour)
    line(points[0],points[1],points[2],points[3])
    line(points[2],points[3],points[4],points[5])
    line(points[4],points[5],points[0],points[1])
    
  def removeGhosting(self,points):
    color("white")
    line(points[0],points[1],points[2],points[3])
    line(points[2],points[3],points[4],points[5])
    line(points[4],points[5],points[0],points[1])
    
    line(points[0],points[1]-1,points[2],points[3]-1)
    line(points[2],points[3]-1,points[4],points[5]-1)
    line(points[4],points[5]-1,points[0],points[1]-1)
    
    line(points[0],points[1]+1,points[2],points[3]+1)
    line(points[2],points[3]+1,points[4],points[5]+1)
    line(points[4],points[5]+1,points[0],points[1]+1)
    
    line(points[0]-1,points[1],points[2]-1,points[3])
    line(points[2]-1,points[3],points[4]-1,points[5])
    line(points[4]-1,points[5],points[0]-1,points[1])
    
    line(points[0]+1,points[1],points[2]+1,points[3])
    line(points[2]+1,points[3],points[4]+1,points[5])
    line(points[4]+1,points[5],points[0]+1,points[1])
    
  
  def move(self,x,y,angle):
    self.removeGhosting(self.points)
    self.draw(x,y,angle,"black")
    
  
color("white")
box(0,0,screen_width,screen_height)

asd = car(100,100,pi/7)

asd.move(150,150,0)