from tealight.art import color,box, polygon,fill_polygon,test_polygon, screen_width, screen_height

class track:
  "Some map disc"
  def __init__(self):
    self.polygons = []
    self.create_polygons()
    self.draw_polygons()
    
    color("white")
    box(0,screen_height/10,screen_width,screen_height)
    
  def create_polygons(self):
    middle = [(screen_width/4,screen_height/4),
              ((3*screen_width/4),screen_height/4),
              ((3*screen_width/4),(3*screen_height/4)),
              (screen_width/4,(3*screen_height/4))]
    self.polygons.append(middle)
    

    
    bottom = [(0,screen_height),
              (screen_width,screen_height),
              (screen_width,(9*screen_height)/10),
              (0,(9*screen_height)/10)]
    self.polygons.append(bottom)
    
    right = [(screen_width,0),
            (screen_width,screen_height),
            ((9*screen_width/10),screen_height),
            ((9*screen_width/10),0)]
    self.polygons.append(right)
    
    left = [(0,(screen_height/10)-3),
             (0,screen_height),
             (screen_width/10,screen_height),
             (screen_width/10,(screen_height/10)-3)]
    self.polygons.append(left)
    
    self.top_detector = [((screen_width*0.45),screen_height/10),
                         ((screen_width*0.45),screen_height/4),
                         ((screen_width*0.55),screen_height/4),
                         ((screen_width*0.55),screen_height/10)]
    self.bottom_detector = [((screen_width*0.45),screen_height*0.9),
                            ((screen_width*0.45),screen_height*0.75),
                            ((screen_width*0.55),screen_height*0.75),
                            ((screen_width*0.55),screen_height*0.9)]
    
  def draw_polygons(self):
    
    color("blue")
    for i in self.polygons:
      fill_polygon(i)
    
    color("red")
    polygon(self.top_detector)
    polygon(self.bottom_detector)
      
  def test_point(self,x,y):
    for i in self.polygons:
      if test_polygon(x,y,i):
        return False
    return True
  
  def test_in_top_detector(self,x,y):
    return test_polygon(x,y,self.top_detector)
  
  def test_in_bottom_detector(self,x,y):
    return test_polygon(x,y,self.bottom_detector)
  