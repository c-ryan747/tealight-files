from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x =        [100,100,100,100,100,100,100]
y =        [100,200,300,400,500,600,700]
vx =       [1,1,1,1,1,1,1]
vy =       [0,0,0,0,0,0,0]
constant = [0,0.625,1.25,2.5,5,7.5,10]

def handle_frame(): 
  global x,y,vx,vy,constant

  for i in range(0,len(x)):
      color("white")
      spot(x[i],y[i],2)
      
      
      angle = math.atan2(-vy[i],vx[i]) + (math.pi / 2)
  
      fx =  1 * math.cos(angle)
      fy = -1 * math.sin(angle)
  
  
      vx[i] = vx[i] + fx
      vy[i] = vy[i] + fy
  
  
      x[i] = x[i] + vx[i]
      y[i] = y[i] + vy[i]
  
  
      color("black")
      spot(x[i],y[i],2)