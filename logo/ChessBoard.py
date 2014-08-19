from tealight.logo import (move, turn)


def whiteSquare(size): #starts + ends top left
  for i in xrange(0,4):
    move(size)
    turn(-90)
    
def blackSquare(size): #starts + ends top left
  for i in xrange(0,4):
    move(size)
    turn(-90)  
    
def chessBoard(gridSize, boxSize):
  for j in xrange(0,gridSize):
    for i in xrange(0,gridSize):
      
      if ((j*gridSize+i)%2 == 0):
        whiteSquare(boxSize)
      else:
        blackSquare(boxSize) 
      
      move(boxSize)
      
    #correct position
    turn(-90)
    move(boxSize)
    turn(-90)
    move(boxSize*gridSize)
    turn(180)

turn(180)  
chessBoard(5,50)
