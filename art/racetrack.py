from tealight.art import (color, image, line, spot, circle, box, image, text, background)

#background ("track.png")

def draw_car(x,y,angle, colour):
  colour(colour)
  line(x,y,100*sin(angle),100*sin(angle))
  
draw_car(200,200,0,"black")