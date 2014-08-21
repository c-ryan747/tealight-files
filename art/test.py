from tealight.art import polygon,fill_polygon,test_polygon, screen_width, screen_height

middle = [(screen_width/4,screen_height/4),
          ((3*screen_width/4),screen_height/4),
          ((3*screen_width/4),(3*screen_height/4)),
          (screen_width/4,(3*screen_height/4))]
top = [(0,0),
       (0,screen_height/10),
       (screen_width,screen_height/10),
       (screen_width,0)]

bottom = [(0,screen_height),
       (screen_width,screen_height),
       (screen_width,(9*screen_height)/10),
       (0,(9*screen_height)/10)]

left = [(screen_width,0),
       (screen_width,screen_height),
       (screen_width/10,screen_height),
       (screen_width/10,0)]

right = [(0,0),
       (0,screen_height),
       (screen_width/10,screen_height),
       (screen_width/10,0)]


fill_polygon(middle)
fill_polygon(top)
fill_polygon(bottom)
fill_polygon(right)
fill_polygon(right)