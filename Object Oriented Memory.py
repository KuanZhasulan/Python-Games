# Create an instance of a Tile object 
import random
import simplegui

TILE_WIDTH = 50
TILE_HEIGHT = 100

click1 = 0
click2 = 0


# definition of empty Tile class (use pass in the body)
class Tile:
    def __init__(self, num, exp, pos):
         self.number = num
         self.exposed = exp
         self.position = pos
        
    def get_number(self):
        return self.number
    def set_number(self, num):
        self.number = num
    def is_exposed(self):
        return self.exposed
    def expose_tile(self):
        self.exposed = True
    def hide_tile(self):
        self.exposed = False
     
    def is_selected(self, pos):
        if self.position[0] <= pos[0] and self.position+TILE_WIDTH > pos[0] and self.position[1] >= pos[1] and pos[1]>=0:
            return True
        else:
            return False
   
    def draw_tile(self, canvas):
        if self.exposed:
            canvas.draw_text(str(self.number), self.position, 20, "Red")
        else:
            canvas.draw_polygon([self.position,
                                 [self.position[0]+TILE_WIDTH,
                                  self.position[1]], 
                                 [self.position[0]+TILE_WIDTH, 
                                  self.position[1]-TILE_HEIGHT], 
                                 [self.position[0], self.position[1]-TILE_HEIGHT]],
                                 1, 'Black', 'Green')  
               
    def __str__(self):
        s = ''
        s += "Number is " + str(self.number)
        s += ", Exposed is "+str(self.exposed)
        return s
    
#################################################
# Student adds code where appropriate
def new_game():
    global click1, click2, score, state, dec 
    score = 0
    state = 0
    dec = []
    for i in range(16):
        t = Tile(i%8, False, [TILE_WIDTH*i, TILE_HEIGHT])
        dec.append(t)
    random.shuffle(dec)    
    
    

def draw(canvas):
    for t in dec:
        t.draw_tile(canvas)

def click(pos):
    global state, score, click1, click2
    choice = list(pos)
    
###################################################
# Testing code 


frame = simplegui.create_frame("Memory", 800, 100)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
new_game()
frame.start()

####################################################
# Output of testing code

#<__main__.Tile object>
#<class '__main__.Tile'>
#<__main__.Tile object>
#<class '__main__.Tile'>