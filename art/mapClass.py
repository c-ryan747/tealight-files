from tealight.art import color,box, polygon,fill_polygon,test_polygon, screen_width, screen_height
from math import pi,sin,cos

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
    middle = self.circle_points_b(sides, screen_width/8,(5*screen_width)/8,(3*screen_height)/8,middle)
    middle = self.circle_points_c(sides, screen_width/8,(5*screen_width)/8,(5*screen_height)/8,middle)
    middle = self.circle_points_d(sides, screen_width/8,(3*screen_width)/8,(5*screen_height)/8,middle)
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