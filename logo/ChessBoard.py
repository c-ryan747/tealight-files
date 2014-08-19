from tealight.logo import (move, turn)


def drawSquare(size): #starts + ends top left
  for i in xrange(0,4):
    move(size)
    turn(90)
  turn(30)
    
def chessBoard(gridSize, boxSize):
  for i in xrange(0,gridSize):
    for j in xrange(0,gridSize):
      drawSquare(boxSize)
      move(boxSize)
    if (i%2 == 0):
      turn(90)
    else:
      turn(270)
    
    move(boxSize*2)
    turn(90)

     
turn(180) #face down
drawSquare(50)
move(100)