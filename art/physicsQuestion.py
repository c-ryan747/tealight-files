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
  
  
  angle = math.atan2(dy,dx) + (math.pi / 2)
  
  fx = math.cos(angle)
  fy = math.sin(angle)
  
  vx = fx 
  vy = fy 
  
  x = x + vx + 0 
  y = y + vy
  

  
  color("blue")
  
  spot(x,y,8)
  