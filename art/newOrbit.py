from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0
friction = 0.1
gravity = 0.15

power = 0.3

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
    
def apply_gravity():
  global x,y,vx,vy,ax,ay,friction
  vy = vy +  + gravity

def apply_friction():
  global x,y,vx,vy,ax,ay,friction
  if vx > friction:
    vx = vx - friction
  elif vx < -friction:
    vx = vx + friction
  else:
    vx = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay,friction
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  
  vy = vy + ay
 
  apply_friction()
  apply_gravity()
  
  x = x + vx
  y = y + vy
 
  
  color("blue")
  
  spot(x,y,8)
  
  
