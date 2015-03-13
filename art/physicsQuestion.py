from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 100
y = 200
vx = 0
vy = 10
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  
  dx = 200 - x
  dy = 200 - y
  
  fx = (dx) / (math.sqrt(dx*dx + dy*dy))
  fy = (dy) / (math.sqrt(dx*dx + dy*dy))
  
  vx = fx + vx
  vy = fy + vy
  
  x = x + vx + 10
  y = y + vy
  

  
  color("blue")
  
  spot(x,y,8)
  