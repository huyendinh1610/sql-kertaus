import sqlite3 #sqlite3 tulee python-asennuksen mukana
import re # regular expression

_IDENTIFIER_RE = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')
#luo db-tiedoston, jos sitä ei ole
conn = sqlite3.connect("test.db") # create or connect 

# luodaan kursori
cursor = conn.cursor() #python pipline 

def create_table(): 
    # annetaan kursorille sql-lause
    cursor.execute("create table if not exists tyontekija(id integer primary key autoincrement, name text not null);")

    # commit-tulee käyttää insert, update, delete 
    # oletuksena sqlite:ssa auto-commit mode päällä
    conn.commit() # tallentaa muutokset pysyvästi

def insert_to_table():
#region
    # huono tapa, mahdolistaa sql-injektion, 
    # (jso käyttäjän nimeä vaikka kysytään, hän voi syöttää nimen sijaan vahingollista sql-syntaksia)
    # cursor.execute("insert into tyontekija(name) values('"+ user_name +"');")
#endregion

    # parempi tapa: (estää sql-injektion)
    cursor.execute("Insert into tyontekija (name) values(?)",("AkuAnkka",))
    conn.commit()

#insert_to_table()

def insert_to(conn: sqlite3.Connection, table, columns: list, values: list) -> None:
    if not _IDENTIFIER_RE.match(table):
        raise ValueError(f"Invalid table name")
    cols = ",".join(columns)
    placeholders = ",".join(["?"]*len(values))
    sql = f"Insert into {table} ({cols}) values({placeholders})"

    cursor = conn.cursor()

    try: 
        cursor.execute(sql, values)
        conn.commit()
        #lisää teksti täällä
    # except(): jos halutaan logata tiedostoon tai konsoliin jotain 
    finally:
        cursor.close()
        #conn.close()

insert_to(conn, "tyontekija", ["name"], ["Batman"]) # should use list instead of tuple
conn.close()

