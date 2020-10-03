#!/usr/bin/env python3
import sqlite3
#connect to db file
dbConnect = sqlite3.connect("temps.db");
#to access columns by name
dbConnect.row_factory = sqlite3.Row;
#create cursor
cursor = dbConnect.cursor();
#execute insert statement
cursor.execute('''insert into temps values('2020-10-02', '14:38:43', 'kitchen', 23.0)''');
dbConnect.commit();
#execute select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
	print(row['tdate'], row['ttime'], row['zone'], row['temperature']);
#close connection
dbConnect.close(); 
