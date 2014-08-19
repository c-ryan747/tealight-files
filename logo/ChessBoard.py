from tealight.logo import (move, turn)


def drawSquare(size):
  for i in xrange(0,4):
    turn(90)
    move(size)
    
    
def chessBoard(gridSize, boxSize):
  for i in xrange(1,2):
    for j in xrange(1,gridSize):
      drawSquare(boxSize)
      move(boxSize)
     
chessBoard(5,10)