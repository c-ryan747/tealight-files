from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

    
while True:
  move()
  if (touch() != "wall"):
    a = 1
  elif (touch() == "wall" and right_side() != "wall"):
    turn(1)
  elif (touch() == "wall" and left_side() != "wall"):
    turn(-1)