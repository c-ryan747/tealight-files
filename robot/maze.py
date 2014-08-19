from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def moveGuy():
  move()
  if (right_side != "wall"):
    turn(1)
  moveGuy()
  
moveGuy()
