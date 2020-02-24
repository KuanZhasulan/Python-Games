# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
              

    def __str__(self):
        s = ''
        s += 'Cards in hand:\n'
        for card in self.cards:
            s += "Rank: " + card.get_rank()+", Suit: " +card.get_suit()+"\n"
        return s 
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = 0
        ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True
        if not ace:
            return hand_value
        else:
            if hand_value+10 <= 21:
                return hand_value+10
            else:
                return hand_value
        
        
   
    def draw(self, canvas, pos):
        count = 0
        for card in self.cards:
            card.draw(canvas, [pos[0]+CARD_SIZE[0]*count, pos[1]])
            count += 1
            
                
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                newcard = Card(s, r)
                self.cards.append(newcard)
        random.shuffle(self.cards)  

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return random.choice(self.cards)
    
    def __str__(self):
        s = ''
        s += 'Cards in Deck:\n'
        for card in self.cards:
            s += "Rank: " + card.get_rank()+", Suit: " +card.get_suit()+"\n"
        return s 


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, new_player, dealer_hands
    deck = Deck()
    deck.shuffle()
    new_player = Hand()
    dealer_hands = Hand()
    new_player.add_card(deck.deal_card())
    new_player.add_card(deck.deal_card())
    dealer_hands.add_card(deck.deal_card())
    dealer_hands.add_card(deck.deal_card())
    # your code goes here
    outcome = ""    
    in_play = True

def hit():
    global new_player, outcome, in_play
    if new_player.get_value() <= 21 and in_play:
        new_player.add_card(deck.deal_card())
    if new_player.get_value()> 21:
        outcome = "You have busted!!!"
        in_play = False
        
    # replace with your code belo
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play
    # replace with your code below
    if new_player.get_value()> 21:
        outcome = "You have busted!!!"
        in_play = False
    if in_play:
        while dealer_hands.get_value() < 17:
            dealer_hands.add_card(deck.deal_card())
        if dealer_hands.get_value() >21:
            outcome = "Dealer Busted!!!"
            in_play = False
        else:
            if dealer_hands.get_value() >= new_player.get_value():
                outcome = "You have lost!!!"
                in_play = False
            else:
                outcome  = "You have won"
                in_play = False
        
    
        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    global new_player, dealer_hands, outcome
    
    new_player.draw(canvas, [100, 100])
    canvas.draw_text("Player's Hand", [100, 50], 50, "Red")
    dealer_hands.draw(canvas, [100, 300])
    canvas.draw_text("Dealer's Hand", [100, 250], 50, "Black")
    canvas.draw_text(outcome, [400, 50], 20, "Aqua")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100+CARD_BACK_CENTER[0], 300+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric