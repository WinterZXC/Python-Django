import psycopg2

conn = psycopg2.connect(dbname="companiestest", user="postgres", password="thisispassword", host="127.0.0.1")
cursor = conn.cursor()

cursor.execute("INSERT INTO main_users (name, surname, personal_code) VALUES ('Anton', 'Petrov', '60307110270')")
cursor.execute("INSERT INTO main_users (name, surname, personal_code) VALUES ('Stas', 'Tsal', '61008294285')")
cursor.execute("INSERT INTO main_users (name, surname, personal_code) VALUES ('Pavel', 'Romanov', '48406250010')")
cursor.execute("INSERT INTO main_users (name, surname, personal_code) VALUES ('Vitaliy', 'Gromyako', '34912032764')")
cursor.execute("INSERT INTO main_users (name, surname, personal_code) VALUES ('Oleg', 'Molyar', '48708173772')")

cursor.execute("INSERT INTO main_companies (name, reg_number, date, capital) VALUES ('Swedbank', '1234567', '2023-01-24', '6000')")

cursor.execute("INSERT INTO main_capital (capital, physical_person, founder, companies_id_id, user_id_id) VALUES ('3000', 'True', 'True','1','1')")
cursor.execute("INSERT INTO main_capital (capital, physical_person, founder, companies_id_id, user_id_id) VALUES ('3000', 'False', 'False','1','2')")

conn.commit()
cursor.close()
conn.close()