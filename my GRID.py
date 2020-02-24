# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    ball_pos = [0, 0]
    for ball in range(GRID_SIZE):
        if ball ==0:
            ball_pos[1] = 20*(ball) + 20 
        else:
            ball_pos[1] = 40*(ball) +20
        for ball in range(GRID_SIZE):
            if ball ==0:
                ball_pos[0] = 20*(ball) +20
            else:
                ball_pos[0] = 40*(ball) +20
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White")
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

