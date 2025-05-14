from flask import Flask, render_template, redirect, url_for, request

import psycopg2

app = Flask(__name__)

    
conn = psycopg2.connect(host='localhost', dbname='Toiletries', user='postgres', password='Postgre', port=5432)
cur = conn.cursor()
cur.execute("""insert into reservation (name, price, date_hour)
values ('Alain Terieur', 50, '2025-06-25')
""")

conn.commit()
cur.close()
conn.close()


@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)