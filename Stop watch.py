# template for "Stopwatch: The Game"
import simplegui
# define global variables
WIDTH = 200
HEIGHT = 200
counter = 0
Y = 0 # total stop times
X = 0 # successful stop times
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = '0'
    B = '0'
    C = '0'
    D = '0'
    milli_second = t%10
    D = str(milli_second)
    remaining = t // 10
    if remaining >= 60:
        second = remaining % 60
        minute = remaining // 60
        A = str(minute)
    else:
        second = remaining
    
    if second < 10:
        C = str(second)
    else:
        tens = second //10
        B = str(tens)
        nums = second % 10
        C = str(nums)
        
    return A+':'+B+C+'.'+D
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    timer.stop()
    global X, Y, running
    if running:
        Y += 1
        if counter % 10 == 0:
            X += 1
            
    running = False
    
def reset():
    timer.stop()
    global counter, X, Y
    counter = 0
    X = 0
    Y = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [WIDTH/2-36, HEIGHT/2], 36, 'Red')
    canvas.draw_text(str(X)+'/'+str(Y), [WIDTH-36, 24], 24, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
