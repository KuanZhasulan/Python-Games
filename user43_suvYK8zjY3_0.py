# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
vel = [0, 0]
ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keyup(key):
    vel[0] = 0
    vel[1] = 0
    
    
def keydown(key):
    value = 5
    if key == simplegui.KEY_MAP["left"]:
        vel[0] = -value
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] = value
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] = value
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] = -value        
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
