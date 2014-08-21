from tealight.art import (color, image, line, spot, circle, box, image, text, background)
from math import sin, cos, pi

#background ("track.png")

def draw_car(x,y,angle, col):
  color(col)
  line(x-100*sin(angle),y-100*cos(angle),x,y)
  line(x-100*sin(angle+(2*pi/3)),y-100*cos(angle+(2*pi/3)),x,y)
  line(x-100*sin(angle+(4*pi/3)),y-100*cos(angle+(4*pi/3)),x,y)
  
  
  
  
draw_car(200,200,0,"black")