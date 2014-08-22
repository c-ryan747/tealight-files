from tealight.art import (fill_polygon, color, line, spot, circle, box, image, text, background, polygon)
import random
from math import cos, sin, pi
import math

from tealight.art import screen_width, screen_height, test_polygon
from tealight.utils import github_load, sleep
#foo = github_load("c-ryan747", "art", "carClass")
#foo2 = github_load("c-ryan747", "art", "mapClass")

#stuff from c-ryan747
from tealight.art import (screen_width, color, image, line, spot, circle, box, image, text, background)
from math import sin, cos, pi
from tealight.art import color,box, polygon,fill_polygon,test_polygon, screen_width, screen_height
from math import pi,sin,cos

hue = 0
  
class car:
  "Race car class"
  
  def __init__(self,x,y,angle):
    self.draw(x,y,angle)
    
    
  def draw(self,x,y,angle):
    size = screen_width/24

    self.points = [x+size*cos(angle),
                   y-size*sin(angle),
                   x+(size/2)*cos(angle+(2*pi/3)),
                   y-(size/2)*sin(angle+(2*pi/3)),
                   x+(size/2)*cos(angle+(4*pi/3)),
                   y-(size/2)*sin(angle+(4*pi/3))]
    
    self.draw_points(self.points)
  
  
  def draw_points(self,points):
    global hue
    color("hsl(%d,100%%,40%%)" % hue)
    hue = hue + 1
    line(points[0],points[1],points[2],points[3])
    line(points[2],points[3],points[4],points[5])
    line(points[4],points[5],points[0],points[1])
    
  
  def move(self,x,y,angle):
    #self.draw_points(self.points,"white")
    self.draw(x,y,angle)
    
    

class track:
  "Some map desc"
  def __init__(self):
    self.polygons = []
    self.top = []
    
    color("white")
    box(0,screen_height/10,screen_width,screen_height)
    
    self.create_polygons()
    self.draw_polygons()
    
    
  def create_polygons(self):
    
    middle = []
    sides = 10
    middle = self.circle_points_a(sides, screen_width/8,(3*screen_width)/8,(3*screen_height)/8,middle)
    #middle = self.circle_points_b(sides, screen_width/8,(5*screen_width)/8,(3*screen_height)/8,middle)
    #middle = self.circle_points_c(sides, screen_width/8,(5*screen_width)/8,(5*screen_height)/8,middle)
    #middle = self.circle_points_d(sides, screen_width/8,(3*screen_width)/8,(5*screen_height)/8,middle)
    self.polygons.append(middle)
    
    self.top = [(0,0),
                (0,screen_height/10),
                (screen_width,screen_height/10),
                (screen_width,0)]
    
    bottom = [(0,screen_height),
              (screen_width,screen_height),
              (screen_width,(9*screen_height)/10),
              (0,(9*screen_height)/10)]
    self.polygons.append(bottom)
    
    right = [(screen_width,screen_height/10),
             (screen_width,screen_height),
             ((9*screen_width/10),screen_height),
             ((9*screen_width/10),screen_height/10)]
    self.polygons.append(right)
    
    left = [(0,(screen_height/10)-3),
            (0,screen_height),
            (screen_width/10,screen_height),
            (screen_width/10,(screen_height/10)-3)]
    self.polygons.append(left)
    
    self.top_detector = [((screen_width*0.45),screen_height/10),
                         ((screen_width*0.45),screen_height/3),
                         ((screen_width*0.55),screen_height/3),
                         ((screen_width*0.55),screen_height/10)]
    self.bottom_detector = [((screen_width*0.45),screen_height*0.9),
                            ((screen_width*0.45),screen_height*0.66),
                            ((screen_width*0.55),screen_height*0.66),
                            ((screen_width*0.55),screen_height*0.9)]
    
  def draw_polygons(self):
    color("red")
    polygon(self.top_detector)
    polygon(self.bottom_detector)
    color("blue")
    for i in self.polygons:
      fill_polygon(i)
    
 
  def test_point(self,x,y):
    if test_polygon(x,y,self.top):
      return False
    for i in self.polygons:
      if test_polygon(x,y,i):
        return False
    return True
  
  
  def test_in_top_detector(self,x,y):
    return test_polygon(x,y,self.top_detector)
  
  
  def test_in_bottom_detector(self,x,y):
    return test_polygon(x,y,self.bottom_detector)
  
  
  #Really this should be only 1 function but its 4 due to time
  #each one draws part of a circle at an offset 
  def circle_points_a(self,amount,radius,cx,cy,array):
    angle = 0
    offset = pi/2
    for j in xrange(0,4):
      angle = offset * j
      for i in xrange(1,amount+2):
        x = cx- (cos(angle)*radius) 
        y = cy-(sin(angle)*radius)
        array.append((x,y))
        #print("x:",str(x),"y:",str(y))
        angle = angle + (pi/2)/amount
    return array
  
  
  def circle_points_b(self,amount,radius,cx,cy,array):
    angle = 0
    for i in xrange(1,amount+2):
      x = cx+(sin(angle)*radius) 
      y = cy-(cos(angle)*radius)
      array.append((x,y))
      #print("x:",str(x),"y:",str(y))
      angle = angle + (pi/2)/amount
    return array 
  
  
  def circle_points_c(self,amount,radius,cx,cy,array):
    angle = 0
    for i in xrange(1,amount+2):
      x = cx+(cos(angle)*radius) 
      y = cy+(sin(angle)*radius)
      array.append((x,y))
      #print("x:",str(x),"y:",str(y))
      angle = angle + (pi/2)/amount
    return array
  
  
  def circle_points_d(self,amount,radius,cx,cy,array):
    angle = 0
    for i in xrange(1,amount+2):
      x = cx-(sin(angle)*radius) 
      y = cy+(cos(angle)*radius)
      array.append((x,y))
      #print("x:",str(x),"y:",str(y))
      angle = angle + (pi/2)/amount
    return array 

#end ofstuff from c-ryan747






# Car stats
acc = 0.3
max_speed = 10
turn_speed = 0.07
friction = 0.05

# Bounce stats
side_bounce = -2

sleep(100)

player_won = 0

lap1 = 1
lap2 = 1
time = 0

car_x = 200
car_y = 160
car_v = 0
car_a = 0
direction = 0
spin = 0

car_x2 = 200
car_y2 = 240
car_v2 = 0
car_a2 = 0
direction2 = 0
spin2 = 0

player_1 = car(car_x,car_y,direction)
player_2 = car(car_x2,car_y2,direction2)
track = track()

##########################################################
### Frame event
##########################################################

def handle_frame():
  global time, friction, car_x, car_y, car_v, car_a, direction, lap1, car_x2, car_y2, car_v2, car_a2, direction2, lap2, player_won
  
  # refreshes screen
  color("rgba(255,255,255,0.1)")
  
  
  box(0,screen_height/10,screen_width,screen_height/10*9)
  
  # Does time
  if lap1 < 4:
    time = time + 0.04
  color( "rgba(150,150,150,0.7)")
  box(0,0,screen_width,screen_height/10)
  color("blue")
  #text(40,20,str(math.ceil(time)))
  text(180,20,"Polygon Racers!")
  text(20,50,"arrow keys lap: " + str(math.floor(lap1))[0]+"/4")
  text(280,50,"wasd keys lap: " + str(math.floor(lap2))[0]+"/4")
  # Does laps for player 1
  if track.test_in_top_detector(player_1.points[0],player_1.points[1]) == True:
    if ((lap1-0.5) % 1) == 0:
      lap1 = lap1 + 0.5
      if lap1 == 4.0 and lap2 < 4:
        player_won = 1
  if track.test_in_bottom_detector(player_1.points[0],player_1.points[1]) == True:
    if (lap1 % 1) == 0:
      lap1 = lap1 + 0.5
   
  # Does laps for player 2
  if track.test_in_top_detector(player_2.points[0],player_2.points[1]) == True:
    if ((lap2-0.5) % 1) == 0:
      lap2 = lap2 + 0.5
      if lap2 == 4.0 and lap1 < 4:
        player_won = 2
  if track.test_in_bottom_detector(player_2.points[0],player_2.points[1]) == True:
    if (lap2 % 1) == 0:
      lap2 = lap2 + 0.5   
  
  
  ################################
  # Collisions with the polygons
  ################################
  
  if not track.test_point(player_1.points[0],player_1.points[1]):
    car_v = car_v*-0.6
    car_x = car_x + -5 * cos(direction)
    car_y = car_y - -5 * sin(direction)
    
  if not track.test_point(player_1.points[2],player_1.points[3]):
    if car_v > 0:
      car_v = car_v*-0.6
      if track.test_point(player_1.points[2],player_1.points[3]):
        car_x = car_x - side_bounce * sin(direction)
        car_y = car_y + side_bounce * cos(direction)
    else:
      #if track.test_point(player_1.points[0],player_1.points[1]):
      
      car_v = 5
      #if track.test_point(player_1.points[0],player_1.points[1]):
      #car_x = car_x - 4 * sin(direction+(pi/2))
      #car_y = car_y + 4 * cos(direction+(pi/2))
      #print "should be working"
  
  elif not track.test_point(player_1.points[4],player_1.points[5]):
    if car_v > 0:
      car_v = car_v*-0.6
      if track.test_point(player_1.points[2],player_1.points[3]):
        car_x = car_x - side_bounce * sin(direction)
        car_y = car_y + side_bounce * cos(direction)
    else:
      car_v = 5
      #if track.test_point(player_1.points[0],player_1.points[1]):

      #if track.test_point(player_1.points[0],player_1.points[1]):
      #car_x = car_x - 4 * sin(direction-(pi/2))
      #car_y = car_y + 4 * cos(direction-(pi/2))
      #print "should be working2"
  
  
  #############################
  # Colisions for second car
  
  if not track.test_point(player_2.points[0],player_2.points[1]):
    car_v2 = car_v2*-0.6
    car_x2 = car_x2 + -5 * cos(direction2)
    car_y2 = car_y2 - -5 * sin(direction2)
    
  if not track.test_point(player_2.points[2],player_2.points[3]):
    if car_v2 > 0:
      car_v2 = car_v2*-0.6
      if track.test_point(player_2.points[2],player_2.points[3]):
        car_x2 = car_x2 - side_bounce * sin(direction2)
        car_y2 = car_y2 + side_bounce * cos(direction2)
    else:
      car_v2 = 2
      #car_x = car_x - 10 * sin(direction)
      #car_y = car_y + 10 * cos(direction)
      #print "should be working"
  
  if not track.test_point(player_2.points[4],player_2.points[5]):
    if car_v2 > 0:
      car_v2 = car_v2*-0.6
      if track.test_point(player_2.points[2],player_2.points[3]):
        car_x2 = car_x2 - side_bounce * sin(direction2)
        car_y2 = car_y2 + side_bounce * cos(direction2)
    else:
      car_v2 = 2
      #car_x = car_x - 10 * sin(direction)
      #car_y = car_y + 10 * cos(direction)
      #print "should be working2"
      
      
      
      
  ##########
  # Physics
  
  #car1
  if car_v > 0:
    car_v -= friction
  else:
    car_v += friction
    
  car_v = min(car_v + car_a,10)
  
  car_x = car_x + car_v * cos(direction)
  car_y = car_y - car_v * sin(direction)

  direction = direction + spin*min(1,car_v/5)
  
  #car2
  if car_v2 > 0:
    car_v2 -= friction
  else:
    car_v2 += friction
    
  car_v2 = min(car_v2 + car_a2,10)
  
  car_x2 = car_x2 + car_v2 * cos(direction2)
  car_y2 = car_y2 - car_v2 * sin(direction2)

  direction2 = direction2 + spin2*min(1,car_v2/5)
  
  ################
  # Drawing bits
  ################
  color("black")
  track.draw_polygons()
  player_1.move(car_x,car_y,direction)
  player_2.move(car_x2,car_y2,direction2)
  
  if player_won == 1:
    image(screen_width/2 - 320,screen_height/2 - 200,"http://i.imgur.com/OQ5AJok.png")
  if player_won == 2:
    image(screen_width/2 - 320,screen_height/2 - 200,"http://i.imgur.com/Bzd2sgV.png")

    
  
##########################################################
### Keypressing events
##########################################################
  
def handle_keydown(key):
  global spin, turn_speed, car_a, acc, spin2, car_a2
  
  if key == "left":
    spin = turn_speed
  elif key == "right":
    spin = -turn_speed
  elif key == "up":
    car_a = acc
  elif key == "down":
    car_a = -acc/1.5
    
  if key == "a":
    spin2 = turn_speed
  elif key == "d":
    spin2 = -turn_speed
  elif key == "w":
    car_a2 = acc
  elif key == "s":
    car_a2 = -acc/1.5

def handle_keyup(key):
  global spin, car_a,spin2, car_a2

  if key == "left" or key == "right":
    spin = 0
  elif key == "up" or key == "down":
    car_a = 0
    
  if key == "a" or key == "d":
    spin2 = 0
  elif key == "s" or key == "w":
    car_a2 = 0
    
    
  
def draw_static_things():
  blue_top = [(0,0),
              (0,screen_height/10),
              (screen_width,screen_height/10),
              (screen_width,0)]
  color("blue")
  fill_polygon(blue_top)
  
  
draw_static_things()
