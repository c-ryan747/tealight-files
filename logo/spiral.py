from tealight.logo import move, turn

def spiral(size):
  
  if size > 300: #terminate after 300 rounds
    return
  
  move(size)
  turn(60) #interior angle
  spiral(size + 5) #make new side slightly bigger
  
spiral(0)