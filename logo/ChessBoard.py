from tealight.logo import (move, turn)


def drawSquare(size):
  for i in xrange(0,4):
    move(side)
    turn(90)
    
def chessBoard(gridSize, boxSize):
  for i in xrange(1,gridSize):
    for j in xrange(1,gridSize):
      drawSquare(boxSize)
      move(boxSize)
     
      