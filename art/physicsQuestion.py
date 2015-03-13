from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 300
y = 300
vx = 10
vy = 0
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 4)
  
  fx =  100 * math.cos(angle)
  fy = -100 * math.sin(angle)
  
  # math.sqrt(vx*vx + vy*vy)
  
  
  x = x + vx + fx
  y = y + vy + fy
  
  vx = fx
  vy = fy
  

  
  color("blue")
  
  spot(x,y,8)
  