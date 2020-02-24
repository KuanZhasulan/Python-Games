# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

MAG_SIZE = 120
mag_POS = [CAN_WIDTH // 2, CAN_HEIGHT//2]

# defines event handlers
def click(pos):
    global mag_POS
    mag_POS  = list(pos) 
    
def draw(canvas):
    canvas.draw_image(image, [MAP_WIDTH/2, MAP_HEIGHT/2],
                      [MAP_WIDTH, MAP_HEIGHT],
                       [CAN_WIDTH/2, CAN_HEIGHT/2],
                      [CAN_WIDTH, CAN_HEIGHT])
    map_pos = [mag_POS[0] *3, mag_POS[1]*3]
    canvas.draw_image(image, map_pos, [MAG_SIZE, MAG_SIZE],
                     mag_POS, [MAG_SIZE, MAG_SIZE])

#create a frame
frame = simplegui.create_frame("MAP", CAN_WIDTH, CAN_HEIGHT)
#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
#start a frame
frame.start()