from tealight.art import polygon,fill_polygon,test_polygon, screen_width, screen_height

points = [(screen_width/4,screen_height/4),
          ((3*screen_width/4),screen_height/4),
          ((3*screen_width/4),(3*screen_height/4)),
          (screen_width/4,(3*screen_height/4))]

fill_polygon(points)