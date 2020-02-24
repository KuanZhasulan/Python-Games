import simplegui

# global variables
HEIGTH = 400
WIDTH = 400
position = [WIDTH/2, HEIGTH/2]
current_key = 0
# def handlers and functions
def keyup(key):
    pass
    
def keydown(key):
    global current_key
    current_key = key
    timer1.start()
def tick():
    global current_key
    if current_key == simplegui.KEY_MAP['left']:
        position[0] -= 5
    elif current_key == simplegui.KEY_MAP['right']:
        position[0] += 5
    elif current_key == simplegui.KEY_MAP['down']:
        position[1] += 5
    elif current_key == simplegui.KEY_MAP['up']:
        position[1] -= 5
# def draw handler 
def draw(canvas):
    canvas.draw_circle(position, 20, 2, "White", "White")

# create a frame
f = simplegui.create_frame('MOVING BALL', WIDTH, HEIGTH)


# register handler 
f.set_draw_handler(draw)
f.set_keyup_handler(keyup)
f.set_keydown_handler(keydown)
timer1 = simplegui.create_timer(100, tick)

# start a frame
f.start()