from tealight.logo import (move, turn)


def drawSquare(size):
  for i in xrange(0,4):
    move(size)
    turn(90)
    
def chessBoard(gridSize, boxSize):
  for i in xrange(0,gridSize):
    for j in xrange(0,gridSize):
      drawSquare(boxSize)
      move(boxSize)
    turn(90)
    move(boxSize)
    
    move(boxSize*gridSize)
    turn(-90)
     
chessBoard(5,10)