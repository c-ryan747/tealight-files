from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Following left wall score = 46
def find_fruit():
  for i in range(1,4):
    if (look() == "fruit"):
      return False
    else:
      turn(1)
  return True


while True:
  if (find_fruit()):
    if (left_side() != "wall"):
      turn(-1)
    elif (touch() == "wall" and right_side() != "wall"):
      turn(1)
    elif (touch() == "wall"):
      turn(2)

