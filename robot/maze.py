from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
for i in xrange(1,8):
  move()
  
print(look())
print(touch())
print(smell())
print(left_side())
print(right_side())