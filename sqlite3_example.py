import sqlite3
conn = sqlite3.connect('pets.db')
conn.execute("CREATE TABLE IF NOT EXISTS pets (type, breed, gender, name)")
conn.execute("INSERT INTO pets VALUES ('dog', 'begel', 'male', 'Oscar')")
conn.execute("INSERT INTO pets VALUES ('cat', 'british', 'female', 'Kate')")
conn.execute("INSERT INTO pets VALUES ('cat', 'siberian', 'female', 'Susanna')")
results = conn.execute("SELECT * FROM pets")
print('Pets table:')
for result in results:
	print(result)
print('Pet table:')
conn = sqlite3.connect('pet.db')
results = conn.execute("SELECT * FROM pet")
for result in results:
	print(result)
conn.close()