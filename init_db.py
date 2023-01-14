import sqlite3

connection = sqlite3.connect('database.db')

### Create empty Database 

with open('schema.sql') as f:
    connection.executescript(f.read())

### Add dummy content

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (image, title, material, description) VALUES (?, ?, ?, ?)",
#             ('https://ucarecdn.com/a25ee431-bbd6-482b-8ad6-7b9e7014b82c/', 'An Image Title', 'AI-generated, 2022', 'A description to go along with it')
#             )

connection.commit()
connection.close()