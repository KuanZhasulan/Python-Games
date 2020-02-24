# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
ball_pos = [0 , 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = [[0, (HEIGHT/2)-HALF_PAD_HEIGHT],
               [0 , (HEIGHT/2)+HALF_PAD_HEIGHT],
               [PAD_WIDTH, (HEIGHT/2)+HALF_PAD_HEIGHT],
                [PAD_WIDTH, (HEIGHT/2)-HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH, (HEIGHT/2)-HALF_PAD_HEIGHT],
               [WIDTH, (HEIGHT/2)+HALF_PAD_HEIGHT],
               [WIDTH- PAD_WIDTH, (HEIGHT/2)+HALF_PAD_HEIGHT],
                [WIDTH- PAD_WIDTH, (HEIGHT/2)-HALF_PAD_HEIGHT]]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_vel, RIGHT, LEFT # these are vectors stored as lists
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
    if direction:
        ball_vel[0] = random.randrange(3, 6)
        ball_vel[1] = -1 * random.randrange(2, 6)
    else:
        ball_vel[0] = -1 * random.randrange(3, 6) 
        ball_vel[1] = random.randrange(2, 6)
    print str(score1)+":"+str(score2)   
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    
     
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), [(WIDTH/2)-2*frame.get_canvas_textwidth(str(score1), 20), 20], 20, "Red")    
    canvas.draw_text(str(score2), [(WIDTH/2)+frame.get_canvas_textwidth(str(score2), 20), 20], 20, "Red")    
   
    # update ball
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    if ball_pos[1] >= paddle1_pos[0][1]-BALL_RADIUS and ball_pos[1] <= paddle1_pos[1][1]+BALL_RADIUS and ball_pos[0] <= PAD_WIDTH + BALL_RADIUS or ball_pos[1] >= paddle2_pos[0][1]-BALL_RADIUS and ball_pos[1] <= paddle2_pos[1][1]+BALL_RADIUS and ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = 1.1 * ball_vel[0]
        ball_vel[1] = 1.1 * ball_vel[1]
    elif ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT);    
        
    elif ball_pos[0] >= WIDTH - (BALL_RADIUS+PAD_WIDTH):
        score1 += 1
        spawn_ball(LEFT)
         
    
        
    if paddle1_pos[0][1] <= 0: 
           paddle1_pos[0][1] = 1
           paddle1_pos[1][1] =  1+PAD_HEIGHT
           paddle1_pos[2][1] = 1+PAD_HEIGHT
           paddle1_pos[3][1] = 1 
    elif paddle1_pos[1][1] >= HEIGHT:
           paddle1_pos[1][1] = HEIGHT-1
           paddle1_pos[0][1] =  HEIGHT - PAD_HEIGHT -1
           paddle1_pos[2][1] = HEIGHT-1
           paddle1_pos[3][1] = HEIGHT - PAD_HEIGHT -1
    else:
        paddle1_pos[0][1] +=  paddle1_vel
        paddle1_pos[1][1] +=  paddle1_vel
        paddle1_pos[2][1] +=  paddle1_vel
        paddle1_pos[3][1] +=  paddle1_vel
    
    if paddle2_pos[0][1] <= 0: 
           paddle2_pos[0][1] = 1
           paddle2_pos[1][1] =  1+PAD_HEIGHT
           paddle2_pos[2][1] = 1+PAD_HEIGHT
           paddle2_pos[3][1] = 1 
    elif paddle2_pos[1][1] >= HEIGHT:
           paddle2_pos[1][1] = HEIGHT-1
           paddle2_pos[0][1] =  HEIGHT - PAD_HEIGHT -1
           paddle2_pos[2][1] = HEIGHT-1
           paddle2_pos[3][1] = HEIGHT - PAD_HEIGHT -1
    else:
        paddle2_pos[0][1] +=  paddle2_vel
        paddle2_pos[1][1] +=  paddle2_vel
        paddle2_pos[2][1] +=  paddle2_vel
        paddle2_pos[3][1] +=  paddle2_vel
    
    
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos,
                         1, "White", "White")
    canvas.draw_polygon(paddle2_pos, 1 , "White", "White") 
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -6
        
    if key == simplegui.KEY_MAP['down']:    
        paddle2_vel = 6
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -6
        
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 6
     
def restart():
    global score1, score2
    new_game();   
    score1= 0
    score2 = 0
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
        
    if key == simplegui.KEY_MAP['down']:    
        paddle2_vel = 0
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 100)

# start frame
new_game()
frame.start()
