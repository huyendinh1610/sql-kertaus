import sqlite3 # tulee python-asennuksen mukana (versiosta 2.5>)

from pathlib import Path
import pandas as pd

# Luodaan tyhjä tiedosto (kuten linuxissa)
#Path('movies.db').touch() # create file 

# Luodaan tietokanta ja kursori
conn = sqlite3.connect('movies.db') # luo tiedoston jos ei löyty

cursor = conn.cursor() 

# cursor.execute("Create table if not exists movies(id int, title text, overview text, " \
#                     "popularity real, release_date text, vote_average real, vote_count int)")

# ota teamista Top_reate_movies1.csv - tiedosto projektikansioon

# luetaan csv-tiedosto pandasin dataframeen
movies = pd.read_csv('Top_rated_movies1.csv')

# kirjoitetaan dataframen sisältö sqlite-tauluuns
movies.to_sql('movies', conn, if_exists='replace', index=False) 
