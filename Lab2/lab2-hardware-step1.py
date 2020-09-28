from sense_hat import SenseHat

sense = SenseHat()

l = (50, 0, 255)
f = (255, 0, 50)
bgc = (0, 255, 0)

# Main Loop

while True:
  event = sense.stick.get_events()
  
  if event:
    
    for e in event:
      if e.action != 'pressed':
        continue
      if e.direction == 'left' or e.direction == 'right' or e.direction == 'down' or e.direction == 'up': 
        while True:
          sense.show_message("A", text_colour = l, back_colour = bgc)
          sense.show_message("S", text_colour = f, back_colour = bgc)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    