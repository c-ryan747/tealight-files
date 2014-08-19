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
      return True
    else:
      turn(1)


while True:
  find_fruit()

