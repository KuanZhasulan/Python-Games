# Testing template for Particle class
import random
import simplegui

###################################################
# Student should add code for the Particle class here
WIDTH = 800
HEIGHT = 600
PARTICLE_RADIUS = 5
COLOR_LIST = ['Green', 'Red', 'Maroon', 
              'Aqua', 'White', 'Blue', 
              'Yellow', 'Navy', 'Brown']
DIRECTION_LIST = [[5, 0], [0, 5], [-5, 0], [0, -5]]

class Particle:
    def __init__(self, position, color):
        self.color = color
        self.pos = list(position)
    
    def move(self, velocity):
        self.pos[0] += velocity[0] 
        self.pos[1] += velocity[1]
        
    def draw(self, canvas):
        canvas.draw_circle(self.pos, PARTICLE_RADIUS, 1, self.color[0], self.color[1])
    def __str__(self):
        return "The Particle is in position " + str(self.position)+" With the colors "+str(self.color)

###################################################
# Test code for the Particle class
def draw(canvas):
    for p in Particles:
        p.move(random.choice(DIRECTION_LIST))
    for p in Particles:
        p.draw(canvas)

Particles = []
for i in range(1000):
    p = Particle([WIDTH/2, HEIGHT/2], [random.choice(COLOR_LIST), random.choice(COLOR_LIST),])
    Particles.append(p)

    
frame = simplegui.create_frame('Balls Moving', WIDTH, HEIGHT)     
frame.set_draw_handler(draw)


frame.start()
##########e#########################################
# Output from test

#Particle with position = [20, 20] and color = Red
#<class '__main__.Particle'>
#Particle with position = [30, 40] and color = Red
#Particle with position = [15, 15] and color = Red
#
#Particle with position = [15, 30] and color = Green
#<class '__main__.Particle'>
#Particle with position = [15, 30] and color = Green
