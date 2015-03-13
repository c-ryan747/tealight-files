from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 400
y = 400
vx = 1
vy = 0
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 2)
  
  fx =  5 * math.cos(angle)
  fy = -5 * math.sin(angle)
  
  # math.sqrt(vx*vx + vy*vy)
  vx = vx + fx
  vy = vy + fy
  
  x = x + vx
  y = y + vy
  

  
  
  color("blue")
  
  spot(x,y,8)
  