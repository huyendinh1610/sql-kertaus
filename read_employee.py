import sqlite3
import pandas as pd

conn = sqlite3.connect('employees.db') ##

cursor = conn.cursor()

cursor.execute("create table if not exists employees (first_name text,last_name text,company_name text,address text,city text,county text,state text,zip text,phone1 text,phone2 text,email text,web text)")

employees = pd.read_csv('us-500.csv')
employees.to_sql('employees', conn, if_exists='replace', index=False) 

data = pd.read_sql("select * from employees", conn)
data.to_csv('newemp.csv')