from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 20
height = 8

def vertical():
  for i in range(0,width):
    for j in range(0,height):
      if i % 4 == 0:
        image(x + i * 60, y + j * 60, "misc/YellowFlower.png")
      else:
        image(x + i * 60, y + j * 60, "misc/Clover.png")
     
def horizontal():
  for i in range(0,width):
    for j in range(0,height):
      if j % 4 == 0:
        image(x + i * 60, y + j * 60, "misc/YellowFlower.png")
      else:
        image(x + i * 60, y + j * 60, "misc/Clover.png")
        

def diagonal():
  is_yellow = False
  for i in range(0,width):
    for j in range(0,height):
      if is_yellow == True:
        image(x + i * 60, y + j * 60, "misc/YellowFlower.png")
        is_yellow = not is_yellow
      else:
        image(x + i * 60, y + j * 60, "misc/Clover.png")
        is_yellow = not is_yellow
        
horizontal()