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
  
  fx =  1 * math.cos(angle)
  fy = -1 * math.sin(angle)
  
  # math.sqrt(vx**2 + vy**2)
  vxa = vx + fx
  vya = vy + fy
  
  vx = math.sqrt(vx**2 + vy**2) * (vxa / (abs(vxa) + abs(vya)))
  vy = math.sqrt(vx**2 + vy**2) * (vya / (abs(vxa) + abs(vya)))
  
  if n < 6:
    print vx, vy
    n = n + 1
  
  
  x = x + vx
  y = y + vy
  

  
  
  color("blue")
  
  spot(x,y,8)
  