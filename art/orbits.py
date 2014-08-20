from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.4
friction = 0.1
gravity = 0.2

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def apply_friction(v):
  if v>0:
    if v>friction:
      v = v - friction
    else:
      v = 0
  elif v<0:
    if v<-friction:
      v = v + friction
    else:
      v = 0
  return v

def apply_gravity (xp,yp):
  global x,y,vx,vy
  deltax = x-xp
  deltay = y-yp
  
  vx = vx + gravity*1
  

  
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  
    
    
  vx = vx + ax
  vy = vy + ay
  
  #friction
  vx = apply_friction(vx)
  vy = apply_friction(vy)
  
  #gravity
  vy = vy + gravity
  
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  