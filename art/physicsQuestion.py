from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 400
y = 400
vx = 10
vy = 0
ax = 0
ay = 0

n = 1

def handle_frame(): 
  global x,y,vx,vy,ax,ay,n
  
  color("white")
  
  spot(x,y,8)

  
  angle = math.atan2(-vy,vx) + (math.pi / 2)
  
  fx =  1 * math.cos(angle)**2
  fy = -1 * math.sin(angle)**2
  
  # math.sqrt(vx**2 + vy**2)
  vx = math.sqrt(vx**2 + vy**2) * fx
  vy = math.sqrt(vx**2 + vy**2) * fy
  
  if n < 50:
    print vx, vy
    n = n + 1
  
  
  x = x + vx
  y = y + vy
  

  
  
  color("blue")
  
  spot(x,y,8)
  