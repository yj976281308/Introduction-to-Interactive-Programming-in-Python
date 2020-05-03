# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

Range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, Range, count
    secret_number = random.randrange(0,Range)
    print 'New game! The range is 0 to '+str(Range)
    if Range == 100:
        count = 7
    elif Range == 1000:
        count = 10
    print 'Number of remaining guess is '+str(count)+'\n'
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global Range
    Range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global Range
    Range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was "+str(guess)
    guess = int(guess)
    global secret_number, count 
    #print "secret number is "+str(secret_number)
    if secret_number == guess:
        count -= 1
        print 'Number of remaining guess is '+str(count)
        print 'Correct\n'
        new_game()
    elif count == 1:
        count -= 1
        print 'Number of remaining guess is '+str(count)
        print 'You ran out of guesses. The number was '+str(secret_number)+'\n'
        new_game()
    elif secret_number > guess:
        count -= 1
        print 'Number of remaining guess is '+str(count)
        print 'Higher\n'
    elif secret_number < guess:
        count -= 1
        print 'Number of remaining guess is '+str(count)
        print 'Lower\n'
        
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame("Guess Number", 100, 200)

# register event handlers for control elements and start frame
frame.add_input("input a number", input_guess, 100)
frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)


frame.start
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
