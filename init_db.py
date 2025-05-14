import psycopg2

conn = psycopg2.connect(host="localhost", dbname="toiletries", user="postgres", password="Ennyfrans1984", port=5432)
cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100), fees integer, duration integer);''')
# cur.execute('''INSERT INTO courses (name, fees, duration) VALUES ('Java', 21, 60)''')

conn.commit()
cur.close()
conn.close()