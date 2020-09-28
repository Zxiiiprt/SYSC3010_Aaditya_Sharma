import urllib.request
import requests
import threading
import json
import random
# all credits go to the YouTube link provided on CuLearn - this code was followed as written by SoumilShah1995(YouTube&GitHub)


# Define a function that will post on server every 15 Seconds
"""def post_data():
    threading.Timer(15,thingspeak_post).start()
    val = random.randint(1,30)
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = ' '
    HEADER = '&field1={}&field2={}'.format(val,val)
    NEW_URL = URl + KEY + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)"""

def read_data():
    URL = 'https://api.thingspeak.com/channels/1160909/feeds.json?api_key='
    KEY = '34BOVG6Y72Q6EEVB'
    HEADER = '&results=5'
    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)
    
    channel_id = get_data['channel']['id']

    feild_1 = get_data['feeds']
    #print(feild_1)

    array = []
    for x in feild_1:
        print(x['field1'])
        array.append(x['field1'])

if __name__ == '__main__':
    #post_data()
    read_data()
