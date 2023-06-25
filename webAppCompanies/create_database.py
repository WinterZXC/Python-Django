import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="thisispassword", host="127.0.0.1")
cursor = conn.cursor()
conn.autocommit = True

sql = "CREATE DATABASE companiestest"

cursor.execute(sql)
cursor.close()
conn.close()