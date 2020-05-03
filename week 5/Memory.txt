# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global lst, exposed, state, counter, card_index
    lst = range(8)+range(8)
    random.shuffle(lst)
    print lst
    exposed = [False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False]
    
    state = 0
    counter = 0
    label.set_text('Turns = '+str(counter))
    card_index = []

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, counter
    
    pos = list(pos)
    i = pos[0]//50
    print i
    if not exposed[i]:
        exposed[i] = True
        counter += 1
        label.set_text('Turns = '+str(counter//2))
        
        card_index.append(i)
        if state == 0:
            state = 1
            
        elif state == 1:
            state = 2
            
                
        else:
            state = 1
            if lst[card_index[0]] != lst[card_index[1]]:
                exposed[card_index[0]] = False
                exposed[card_index[1]] = False
                card_index.pop(0)
                card_index.pop(0)
            else:
                exposed[card_index[0]] = True
                exposed[card_index[1]] = True
                card_index.pop(0)
                card_index.pop(0)
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(lst)):
        if exposed[i]:
            canvas.draw_text(str(lst[i]),[15+50*i,60], 
                         30, 'White')
        else:
            polygon = [(50*i, 0), (50*i+50, 0), (50*i+50, 100),
                       (50*i, 100)]
            canvas.draw_polygon(polygon, 1, 'Red', 'Green')
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric