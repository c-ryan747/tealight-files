from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,800):
  move(i)
  turn(179.9)
  color(colors[i%3])