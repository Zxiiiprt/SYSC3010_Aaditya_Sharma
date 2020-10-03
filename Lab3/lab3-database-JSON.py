from urllib.request import *
from urllib.parse import *
import json

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e09 9a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7" # If it doesn’t work, get your own.

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
# results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

later = data["wind"]
print ("Wind : %d" % later["speed"])

#!/usr/bin/env python3
import sqlite3
#connect to db file
dbConnect = sqlite3.connect("weather.db");
#to access columns by name
dbConnect.row_factory = sqlite3.Row;
#create cursor
cursor = dbConnect.cursor();
#execute insert statement
cursor.execute('''insert into weather values (?, ?, ?, ?, ?)''', (city, current["temp"], current["humidity"], current["pressure"], later["speed"]));
dbConnect.commit();
#execute select statement
cursor.execute('SELECT * FROM weather');
#print data
for row in cursor:
	print("City - ", row['City'], "\n Temperature : ", row['Temp'], degreeSym, "F"+"\n Humidity: ", row['Humidity'], "%"+"\n Pressure: ", row['Pressure'], "\n Wind Speed: ", row['wind'], "\n");
#close connection
dbConnect.close();

