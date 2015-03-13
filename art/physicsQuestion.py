from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 100
y = 200
vx = 10
vy = 0
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(vy,vx) + (math.pi / 2)
  
  fx = 10 *math.cos(angle)
  fy = 10 *math.sin(angle)
  
  vx = fx
  vy = fy
  
  x = x + fx
  y = y + fy
  

  
  color("blue")
  
  spot(x,y,8)
  