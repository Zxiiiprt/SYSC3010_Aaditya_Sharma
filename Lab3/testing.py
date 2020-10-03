import sqlite3

dbConnect = sqlite3.connect("sensors.db")

dbConnect.row_factory = sqlite3.Row

cursor = dbConnect.cursor()

cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"')
print("Sensors in the Kitchen - \n")

for row in cursor:
        print("Sensor ID: ", row['sensorID'], "\n", " Type: ", row['type'])

cursor.execute('SELECT * FROM sensors WHERE type="door"')
print("\nDisplaying all the door sensors - \n")

for row in cursor:
        print("Sensor ID: ", row['sensorID'], "\n", " Zone: ", row['zone'])

dbConnect.close()
