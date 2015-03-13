from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 300
y = 300
vx = math.sqrt(2)
vy = math.sqrt(2)
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 2)
  
  fx =  1 * math.cos(angle)
  fy = -1 * math.sin(angle)
  
  vx = (0 + fx) / (math.sqrt(vx*vx + vy*vy))
  vy = (0 + fy) / (math.sqrt(vx*vx + vy*vy))
  
  x = x + vx
  y = y + vy
  

  
  color("blue")
  
  spot(x,y,8)
  