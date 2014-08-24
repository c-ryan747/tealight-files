from tealight.logo import move, turn

def zig(n):
  if n == 1:
    turn(-45)
    move(5)
    turn(-45)
    move(10)
    turn(-45)
    move(5)
    turn(-45)
    move(10)
  else:
    zig(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)
    
def zag(n):
  if n == 1:
    turn(45)
    move(5)
    turn(45)
    move(10)
    turn(45)
    move(5)
    turn(45)
    move(10)
    turn(-45)
    move(5)
    turn(-45)
    move(10)
  else:
    zag(n/2)
    zag(n/2)
    zig(n/2)
    zag(n/2)
    
zig(8)
zig(8)