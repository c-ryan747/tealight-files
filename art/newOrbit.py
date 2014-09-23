from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = [screen_width / 2]
y = [screen_height / 2]
vx = [0.0]
vy = [0.0]
ax = [0.0]
ay = [0.0]
friction = 0.1
gravity = 0.15

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    for i in xrange(0,len(ax)):
      ax[i] = -power
      print(ax)
  elif key == "right":
    for i in xrange(0,len(ax)):
      ax[i] = power
  elif key == "up":
    for i in xrange(0,len(ay)):
      ay[i] = -power
  elif key == "down":
    for i in xrange(0,len(ay)):
      ay[i] = power
  elif key == "a":
    x.append(screen_width / 2)
    y.append(screen_height / 2)
    vx.append(vx[0])
    vy.append(vy[0])
    ax.append(ax[0])
    ay.append(ay[0])
    

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    for i in xrange(0,len(ax)):
      ax[i] = 0
  elif key == "up" or key == "down":
    for i in xrange(0,len(ay)):
      ay[i] = 0
    
def apply_gravity(v):
  global gravity
  v = v + gravity
  return v

def apply_friction(v):
  global friction
  if v > friction:
    v = v - friction
  elif vx < -friction:
    v = v + friction
  else:
    v = 0
  return v
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  for i in xrange(0,len(x)):  
    color("white")
  
    spot(x[i],y[i],8)
    vx[i] = vx[i] + ax[i]
  
    vy[i] = vy[i] + ay[i]
 
    vx[i] = apply_friction(vx[i])
    vy[i] = apply_gravity(vy[i])
  
    x[i] = x[i] + vx[i]
    y[i] = y[i] + vy[i]
 
  
    color("blue")
  
    spot(x[i],y[i],8)
  
