import sqlite3
conn = sqlite3.connect('pets.db')
conn.execute("CREATE TABLE IF NOT EXISTS pets (type, breed, gender, name)")
conn.execute("INSERT INTO pets VALUES ('dog', 'begel', 'male', 'Oscar')")
conn.execute("INSERT INTO pets VALUES ('cat', 'british', 'female', 'Kate')")
results = conn.execute("SELECT * FROM pets")
for result in results:
	print(result)
conn.close()