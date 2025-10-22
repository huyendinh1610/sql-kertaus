import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()
""" rows = cursor.execute("select * from movies") # return cursor object: sqlite3.Cursor
# print(rows)
# print(type(rows))

# fetchone() palauttaa 1 rivin 
# fetchall() palauttaa listan 
movies = rows.fetchall()
print(movies) """

# helpompi tapa (jos onnistuu) - SQL > CSV pandas dataframella
df = pd.read_sql("select * from movies", conn)
#df.to_csv('elokuvat_sqlsta.csv', index=False)

from skimpy import skim

skim(df)