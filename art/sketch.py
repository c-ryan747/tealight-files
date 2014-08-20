from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0



def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def draw_to(x,y):
  global lastx, lasty
  
  line(lastx, lasty, x, y)
  lastx = x
  lasty = y
  
  
  
def handle_mousemove(x,y,button):
  if button == "right":
    color("black")
    draw_to(x,y)
  elif button == "left":
    color("red")
    draw_to(x,y)
  

 
  