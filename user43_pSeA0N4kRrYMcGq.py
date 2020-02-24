# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
low = 0
high = 100
secret_number = 0
number_of_guesses = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, low, high, number_of_guesses
    number_of_guesses = int(math.log((high - low ), 2)+1)
    secret_number = random.randrange(low, high) 
    print "Number of guesses = "+str(number_of_guesses)




def range100():
    global low, high 
    # button that changes the range to [0,100) and starts a new game 
    low = 0
    high = 100
    new_game()
    # remove this when you add your code        
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    
    global number_of_guesses, secret_number
    number_of_guesses -= 1 
    # remove this when you add your code
   
    guess = int(guess)
    print "Guess was "+str(guess)
    print "The remaining number of guesses = "+str(number_of_guesses)
    if guess > secret_number:
        print "Lower!"
    elif guess < secret_number:
        print "Higher!"
    elif guess == secret_number:
        print "Correct"

    
# create frame
frame = simplegui.create_frame('Guess Machine!!!',
                               200, 200)
input1 = frame.add_input("Guess?", input_guess, 100)
button1 = frame.add_button('range [0, 100)', range100, 100)
button2 = frame.add_button('range [0, 1000)', range1000, 100)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
