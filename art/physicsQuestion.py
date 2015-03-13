from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 300
y = 300
vx = 100
vy = 100
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 2)
  
  fx =  1 * math.cos(angle)
  fy = -1 * math.sin(angle)
  
  # math.sqrt(vx*vx + vy*vy)
  
  vx = 10 * math.sqrt(2) * fx
  vy = 10 * math.sqrt(2) * fy
  
  
  x = x + vx
  y = y + vy
  

  
  color("blue")
  
  spot(x,y,8)
  