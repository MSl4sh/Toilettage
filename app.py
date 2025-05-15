from flask import Flask, render_template, redirect, url_for, request
import psycopg2
# Data-base connection
import psycopg2
import xml.etree.ElementTree as ET
from formulas import Formula

app = Flask(__name__)


# à remplacer par vos identifiants et votre nom de Db étant donné qu'on a pas tous le meme
def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="toiletries", user="postgres", password="Ennyfrans1984",
                            port=5432)
    return conn


def get_formulas():
    formulas = []
    tree = ET.parse('data/formulas.xml')
    root = tree.getroot()
    
    for package_elem in root.findall('package'):
        package_id = package_elem.get('id')
        title = package_elem.find('title').text
        description = package_elem.find('description').text
        price = package_elem.find('price').text
        note = package_elem.find('note').text
        features = [f.text for f in package_elem.findall('feature')]
        formula = Formula(
            package=package_id,
            title=title,
            description=description,
            features=features,
            price=price,
            note=note
        )
        formulas.append(formula)

    return formulas



@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/services')
def services():
    
    
    formulas = get_formulas()

    return render_template('services.html', formulas=formulas)

@app.route("/test")
def test():
    conn = psycopg2.connect(
        "host=localhost dbname=start-pup user=postgres password=postgres port=5432")
    cur = conn.cursor()
    cur.execute(""" insert into reservation (id_traitment, name, price, date_hour)
    values ('1','Jacqueline',50, '2025-06-25 08:00 AM')
    """)
    conn.commit()
    cur.close()
    return redirect("/home")

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

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():

    if request.method == 'POST':
        conn = db_conn()

        formula_id = request.form.get('formula')
        lastname = request.form.get('lastname')
        firstname = request.form.get('firstname')
        date = request.form.get('date')
        time = request.form.get('time')


    formula_id = request.args.get('formula_id')
    
    formulas = get_formulas()

    return render_template("reservation.html", formulas=formulas,formula_id=formula_id)

if __name__ == "__main__":
    app.run(debug=True)
