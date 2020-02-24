# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    polyline.append(pos)
          
# button to clear canvas
def clear():
    remove = []
    for pos in polyline:
        remove.append(pos)
    for pos in remove:
        polyline.remove(pos)
        

# define draw
def draw(canvas):
    if len(polyline) != 0:   
        canvas.draw_polygon(polyline, 1, 'Yellow')
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

