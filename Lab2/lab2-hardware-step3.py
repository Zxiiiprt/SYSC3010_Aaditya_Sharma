from sense_hat import SenseHat
#this code was inspired off the Emulator presented in Part1 Step1 and ThePiMaker(YouTube = https://www.youtube.com/watch?v=a9lHeVIADSQ)

sense = SenseHat()

while True:
    t = round(sense.get_temperature(), 1)
    p = round(sense.get_pressure(), 1)
    h = round(sense.get_humidity(), 1)

    bgc = [50, 0, 255]   

    msg = "Temperature = %s, Pressure = %s, Humidity = %s" % (t, p, h)

    sense.show_message(msg, scroll_speed = 0.08, back_colour = bgc)
