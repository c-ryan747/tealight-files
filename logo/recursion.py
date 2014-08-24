from tealight.logo import move, turn

size = 4

def zig(n):
  if n == 1:
    turn(-45)
    move(size/2)
    turn(-45)
    move(size)
    turn(-45)
    move(size/2)
    turn(-45)
    move(size)
  else:
    zig(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)
    
def zag(n):
  if n == 1:
    turn(45)
    move(size/2)
    turn(45)
    move(size)
    turn(45)
    move(size/2)
    turn(45)
    move(size)
    turn(-45)
    move(size/2)
    turn(-45)
    move(size)
  else:
    zag(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)
    
zig(16)
zig(16)