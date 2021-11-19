import sqlite3

file = "Sqlite3.db"

try:
	conn = sqlite3.connect(file)
	cur = conn.cursor()
	query = cur.execute( "INSERT INTO categories VALUES ('Category', 'First President Of the United States?', 'Abraham Lincoln', 'Quincy Adams', 'James Madison', 'George Washington', 300 )" )
	conn.commit()
	conn.close()
	print("Success")
except Exception as e:
	print(e)
