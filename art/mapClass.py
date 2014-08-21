from tealight.art import color, polygon,fill_polygon,test_polygon, screen_width, screen_height

class track:
  "Some map disc"
  def __init__(self):
    self.polygons = []
    self.detector = []
    self.create_polygons()
    self.draw_polygons()
    
  def create_polygons(self):
    middle = [(screen_width/4,screen_height/4),
              ((3*screen_width/4),screen_height/4),
              ((3*screen_width/4),(3*screen_height/4)),
              (screen_width/4,(3*screen_height/4))]
    self.polygons.append(middle)
    
    top = [(0,0),
           (0,screen_height/10),
           (screen_width,screen_height/10),
           (screen_width,0)]
    self.polygons.append(top)
    
    bottom = [(0,screen_height),
              (screen_width,screen_height),
              (screen_width,(9*screen_height)/10),
              (0,(9*screen_height)/10)]
    self.polygons.append(bottom)
    
    left = [(screen_width,0),
            (screen_width,screen_height),
            ((9*screen_width/10),screen_height),
            ((9*screen_width/10),0)]
    self.polygons.append(left)
    
    right = [(0,0),
             (0,screen_height),
             (screen_width/10,screen_height),
             (screen_width/10,0)]
    self.polygons.append(right)
    
    self.detector = [(screen_width*0.45),screen_width/10),
                     (screen_width*0.45),screen_width/5),
                     (screen_width*0.55),screen_width/5),
                     (screen_width*0.55),screen_width/10)]
    
  def draw_polygons(self):
    color("blue")
    for i in self.polygons:
      fill_polygon(i)
      polygon(self.detector)
      
  def test_point(self,x,y):
    for i in self.polygons:
      if test_polygon(x,y,i):
        return False
    return True
  
  def test_in_detector(x,y):
    return test_polygon(x,y,self.detector)
  
    
    
mainMap = track()
print (mainMap.test_in_detector(screen_width*0.47),screen_width/9))
#print (mainMap.test_point(100,100))
