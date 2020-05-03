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
win = 0
lose = 0

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
        self.card = []
    # create Hand object
    

    def __str__(self):
        s = "Hand contains " 
        for i in self.card:
            s += i.get_suit()
            s += i.get_rank()
            s += ' '
        return s
        # return a string representation of a hand

    def add_card(self, card):
        self.card.append(card)	# add a card object to a hand


    def get_value(self):
        value = 0
        if len(self.card) == 0:
            return value
        else:
            for i in self.card:
                value += VALUES[i.get_rank()]
                
            for i in self.card:
                if i.get_rank() == 'A' and (value + 10) <= 21:
                    value += 10
            return value
            
        
    def draw(self, canvas, pos):
        for c in self.card:
            c.draw(canvas, pos)
            pos[0] += 100 
            # draw a hand on the canvas, use the draw method for cards
                

        
# define deck class 
class Deck:
    def __init__(self):
        self.card = []
        for i in SUITS:
            for j in RANKS:
                self.card.append(Card(i,j))
            # create a Deck object

    def shuffle(self):
        random.shuffle(self.card)
        # shuffle the deck 
            # use random.shuffle()

    def deal_card(self):
        deal = self.card[-1]
        self.card.pop()
        return deal
            # deal a card object from the deck
    
    def __str__(self):
        s = "Deck contains "
        for i in self.card:
            s += i.get_suit()
            s += i.get_rank()
            s += ' '
        return s
            # return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play
    global player, dealer, my_deck, lose
    outcome = "Hit or stand?"
    if in_play:
        lose += 1
    in_play = True
    
    my_deck = Deck()
    my_deck.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        c1 = my_deck.deal_card()
        player.add_card(c1)
        
        c2 = my_deck.deal_card()
        dealer.add_card(c2)
    
    print "Dealer ", dealer
    print "Player ", player
    
    
def hit():
    global in_play, outcome
    global player, lose

    card = my_deck.deal_card()
    player.add_card(card)  
    print "Player ", player
    score_player = player.get_value()
    if score_player > 21:
        outcome = "You have busted, new deal?"
        lose += 1
        in_play = False
        print "Player score is ", score_player
            
def stand():
    global in_play, outcome
    global win, lose
    in_play = False
    while dealer.get_value() < 17:
        card = my_deck.deal_card()
        dealer.add_card(card)
        print "Dealer ", dealer
        
    score_dealer = dealer.get_value()
    print "Dealer score is ", score_dealer
    if score_dealer > 21:
        outcome = "Dealer has busted, new deal?"
        win += 1
    elif score_dealer < player.get_value():
        outcome = "You win, new deal?"
        win += 1
    else: 
        outcome = "You lose, new deal?"
        lose += 1
        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome, [200, 300], 30, 'White')
    canvas.draw_text('Blackjack', [50, 50], 40, 'Black')
    canvas.draw_text('Dealer', [50, 120], 40, 'Red')
    canvas.draw_text('Player', [50, 370], 40, 'Red')
    
    dealer.draw(canvas, [50, 150])
    player.draw(canvas, [50, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [50 + CARD_CENTER[0], 150 + CARD_CENTER[1]], CARD_SIZE)
    
    score = win - lose
    canvas.draw_text("Score: "+str(score), [350, 50], 40, 'Black')
   
        


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