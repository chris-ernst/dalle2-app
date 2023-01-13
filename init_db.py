import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (image, title, material, description) VALUES (?, ?, ?, ?)",
            ('https://ucarecdn.com/a25ee431-bbd6-482b-8ad6-7b9e7014b82c/', 'An Image Title', 'AI-generated, 2022', 'A description to go along with it')
            )

cur.execute("INSERT INTO posts (image, title, material, description) VALUES (?, ?, ?, ?)",
            ('https://ucarecdn.com/a25ee431-bbd6-482b-8ad6-7b9e7014b82c/', 'An Image Title', 'AI-generated, 2022', 'A description to go along with it')
            )

connection.commit()
connection.close()