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
  if (left_side() != "wall"):
    turn(-1)
  elif (right_side() != "wall"):
    turn(1)
  elif (touch() == "wall"):
    turn(2)