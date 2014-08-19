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
      move(1)
      return True
    else:
      turn(1)
  return False

def test_way():
  while True:
    if (find_fruit() == False):
      if (touch() != "wall"):
        a=1
      elif (left_side() != "wall"):
        turn(-1)
      elif (touch() == "wall" and right_side() != "wall"):
        turn(1)
      elif (touch() == "wall"):
        turn(2)
      move()

def left_way():
  while True:
    move()
    if (left_side() != "wall"):
      turn(-1)
    elif (touch() == "wall" and right_side() != "wall"):
      turn(1)
    elif (touch() == "wall"):
      turn(2)
    
test_way()