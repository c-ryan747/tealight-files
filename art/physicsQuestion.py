from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 200
y = 200
vx = 0
vy = 10
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 2)
  
  fx = 1 * math.cos(angle)
  fy = -1 * math.sin(angle)
  
  vx = vx + fx
  vy = vy + fy
  
  x = x + vx
  y = y + vy
  

  
  color("blue")
  
  spot(x,y,8)
  