from flask import Flask, render_template, redirect, url_for, request
import psycopg2



app = Flask(__name__)


# def get_connection():
#         try:
#             conn = psycopg2.connect(
#                 dbname="start-pup",
#                 user="postgres",
#                 host="localhost",
#                 password="postgres"
#             )
#             return conn
#         except psycopg2.OperationalError as e:
#             print(e)

# get_connection()
conn= psycopg2.connect("host=localhost dbname=start-pup user=postgres password=postgres port=5432")
cur=conn.cursor()

cur.execute(""" insert into appointment (appointment_date, hour_start)
values ('2025-06-25', '08:00 AM'), ('2025-06-25', '10:00 AM'), ('2025-06-25', '01:00 PM'), ('2025-06-25', '03:00 PM')
""")
conn.commit()
cur.close()


    
@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
