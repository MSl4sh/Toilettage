from flask import Flask, render_template, redirect, url_for, request
import psycopg2
# Data-base connection
import sqlalchemy

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="toiletries", user="postgres", password="Ennyfrans1984",
                            port=5432)
    return conn


    
@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/reservation")
def reservation():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM reservation''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reservation.html', data=data)

@app.route('/book', methods=['POST'])
def book():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']
    price = request.form['price']
    #date_hour = request.form['date_hour']
    cur.execute('''INSERT INTO reservation(name, price) VALUES(%s,%s)''',(name, price))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('reservation'))

if __name__ == "__main__":
    app.run(debug=True)