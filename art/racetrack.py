from tealight.art import (color, image, line, spot, circle, box, image, text, background)
from math import sin, cos, pi

#background ("track.png")

  
class car:
  "Race car class"
  def __init__(self, x, y, angle):
    draw(x,y,angle)
  def draw(x,y,angle):
    color(col)
    line(x-100*sin(angle),y-100*cos(angle),x-100*sin(angle+(2*pi/3)),y-100*cos(angle+(2*pi/3)))
    line(x-100*sin(angle+(2*pi/3)),y-100*cos(angle+(2*pi/3)),x-100*sin(angle+(4*pi/3)),y-100*cos(angle+(4*pi/3)))
    line(x-100*sin(angle+(4*pi/3)),y-100*cos(angle+(4*pi/3)),x-100*sin(angle),y-100*cos(angle))
  
  


car = car(200,200,0)