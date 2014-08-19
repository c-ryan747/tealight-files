from tealight.logo import (move, turn)


def drawSquare(size): #starts + ends top left
  for i in xrange(0,4):
    move(size)
    turn(-90)
    
def chessBoard(gridSize, boxSize):
  for i in xrange(0,gridSize):
    drawSquare(boxSize)
    move(boxSize)
  turn(-90)
  move(boxSize)
  turn(-90)
  move(boxSize*gridSize)

     
turn(180) #face down
chessBoard(5,50)
move(500)