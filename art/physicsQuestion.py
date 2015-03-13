from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 300
y = 200
vx = 0
vy = 0
ax = 0
ay = 0

def handle_frame(): 
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  
    
  vx = vx + ax
  vy = vy + ay
  
  
  #gravity
  vy = vy + gravity
  apply_gravity()
  
  #friction
  vx = apply_friction(vx)
  vy = apply_friction(vy)
  

  
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  