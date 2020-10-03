from sense_hat import SenseHat

sense = SenseHat()

l = (50, 0, 255)
f = (255, 0, 50)
bgc = (0, 255, 0)

sense.clear()

# The code written underneath is if you wanted to select what pattern exactly you want
# on the 8x8 LED matrix of the Sense Hat
# the logic remains the same, the only thing that changes is the function call
# I found a nicer display with show_message and since we are only displaying letters I thought it was fair to use that
# This was my own personal assumption, and if the lab intended to have a personal logo or display then the folllowing code thats commented out below would be the way to do it

#X = (0, 0, 0)
#N = (50, 0, 255)
# Name Images/LED Pattern

"""def first_initial():
  image = [
    X, X, X, N, N, X, X, X,
    X, X, N, X, X, N, X, X,
    X, X, N, X, X, N, X, X,
    X, X, N, X, X, N, X, X,
    X, N, N, N, N, N, N, X,
    X, X, N, X, X, N, X, X,
    X, X, N, X, X, N, X, X,
    X, X, N, X, X, N, X, X]
  return image
  
def last_initial():
  image = [
    X, X, X, N, N, X, X, X,
    X, X, N, X, X, N, X, X,
    X, X, N, X, X, X, X, X,
    X, X, X, N, N, X, X, X,
    X, X, X, X, X, N, X, X,
    X, X, X, X, X, N, X, X,
    X, X, N, X, X, N, X, X,
    X, X, X, N, N, X, X, X]
  return image"""

i = 2

# Main Loop

while True:
    event = sense.stick.get_events()
    
    if event:
        
        for e in event:
            
            if e.action != 'pressed':
                continue
            
            if e.direction == 'middle':
                sense.clear()
                    
            elif e.direction == 'right' or 'down' or 'up' or 'left': #
                if (i % 2) == 0:
                    sense.show_message("A", text_colour = l, back_colour = bgc) #first_initial()
                    i += 1
                              
                else:
                    sense.show_message("S", text_colour = f, back_colour = bgc) #last_initial()
                    i += 1

