from tealight.art import (color, line, spot, circle, box, image, text, background)
import math

x =        [100,100,100,100,100,100,100]
y =        [100,200,300,400,500,600,700]
vx =       [5,5,5,5,5,5,5]
vy =       [0,0,0,0,0,0,0]
constant = [0,0.2,1.25,2.5,5,7.5,10]

def handle_frame(): 
  global x,y,vx,vy,constant

  for i in range(0,len(x)):
      color("white")
      spot(x[i],y[i],2)
      
      
      angle = math.atan2(-vy[i],vx[i]) + (math.pi / 2)
  
      fx =  1 * math.cos(angle)
      fy = -1 * math.sin(angle)
  
  
      vxa = vx[i] + fx
      vya = vy[i] + fy
  
      factor = math.sqrt(vx[i]**2 + vy[i]**2) / math.sqrt(vxa**2 + vya**2)
  
      vx[i] = vxa * factor  + constant[i]
      vy[i] = vya * factor 
  
  
      x[i] = x[i] + vx[i]
      y[i] = y[i] + vy[i]
  
  
      color("black")
      spot(x[i],y[i],2)