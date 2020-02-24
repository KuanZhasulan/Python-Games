# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = (math.pi -1.6)/ 2
firing_angle_vel = 0
bubble_stuck = True
vector = [0, 0]
firing_line = [0, 0]
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# class defintion for Bubbles
class Bubble:
    
    def __init__(self, pos, color, vel = [0, 0]):
        self.pos = [pos[0], pos[1]] 
        self.vel = [vel[0], vel[1]]
        self.color = color
    
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    def fire_bubble(self, vel):
        self.vel = list([vel[0], vel[1]])
        firing_sound.play()
    def is_stuck(self): 
        pass

    def collide(self, bubble):
        pass
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, self.color, self.color)
        

# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck, vector
    if key == simplegui.KEY_MAP['left']:
        firing_angle_vel += FIRING_ANGLE_VEL_INC
    elif key == simplegui.KEY_MAP['right']:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC
        
    if key == simplegui.KEY_MAP['space']:
        a_bubble.fire_bubble([vector[0]*3, -vector[1]*3])
    
def keyup(key):
    global firing_angle_vel
    if key ==  simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right']:
        firing_angle_vel = 0
    
# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck, firing_line, vector
    
    # update firing angle
    firing_angle += firing_angle_vel
    vector = angle_to_vector(firing_angle)
    firing_line[0] = FIRING_POSITION[0]+vector[0]*FIRING_LINE_LENGTH
    firing_line[1] = FIRING_POSITION[1]-vector[1]*FIRING_LINE_LENGTH
    # draw firing line
    canvas.draw_line(FIRING_POSITION, firing_line, 2, "White")
    # update a_bubble and check for sticking
    
    a_bubble.update()
    
    
    a_bubble.draw(canvas)
    # draw a bubble and stuck bubbles
 
# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
a_bubble = Bubble(FIRING_POSITION, random.choice(COLOR_LIST))
frame.start()