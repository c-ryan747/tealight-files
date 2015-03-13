from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 0
y = 400
vx = 5
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
  
  
  vxa = vx + fx
  vya = vy + fy
  
  factor = math.sqrt(vx**2 + vy**2) / math.sqrt(vxa**2 + vya**2)
  
  vx = vxa * factor
  vy = vya * factor
  
  
  x = x + vx + 2.5
  y = y + vy
  
  
  color("blue")
  spot(x,y,8)