from tealight.art import polygon,fill_polygon,test_polygon, screen_width, screen_height

class map:
  "Some map disc"
  def __init__(self):
    self.polygons = []
    self.create_polygons()
    self.draw_polygons()
    
  def create_polygons:
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
    
  def draw_polygons:
    color("blue")
    for i in self.polygons:
      fill_polygon(i)
    
    
mainMap = map()
