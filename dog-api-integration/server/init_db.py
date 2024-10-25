import sqlite3
import csv

conn = sqlite3.connect('images.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL
)
''')

with open('dog_images.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        url, width, height = row[1], int(row[2]), int(row[3])
        cursor.execute('INSERT INTO images (url, width, height) VALUES (?, ?, ?)',
                       (url, width, height))
conn.commit()
conn.close()
