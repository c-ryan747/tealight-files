from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 200
y = 200
vx = 100
vy = 0
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(y - vy,x - vx) + (math.pi / 2)
  
  fx = 100 *math.sin(angle)
  fy = 100 *math.cos(angle)
  
  vx = fx
  vy = fy
  
  x = x + fx
  y = y + fy
  

  
  color("blue")
  
  spot(x,y,8)
  