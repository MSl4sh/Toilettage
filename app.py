from flask import Flask, render_template, redirect, url_for, request
import psycopg2
import xml.etree.ElementTree as ET
from formulas import Formula



app = Flask(__name__)



    
@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/services')
def services():
    tree = ET.parse('data/formulas.xml')
    root = tree.getroot()
    
    formulas = []
    
    
    for package_elem in root.findall('package'):
        package_id = package_elem.get('id')
        title = package_elem.find('title').text
        description = package_elem.find('description').text
        price = package_elem.find('price').text
        note = package_elem.find('note').text
        features =[]
        features.append(package_elem.find('first_feature').text)
        features.append(package_elem.find('second_feature').text)
        features.append(package_elem.find('third_feature').text)
        features.append(package_elem.find('fourth_feature').text)
        print(package_elem.find('first_feature').text)
        formula = Formula(
            package=package_id,
            title=title,
            description=description,
            features=features,
            price=price,
            note=note
        )
        formulas.append(formula)

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


if __name__ == "__main__":
    app.run(debug=True)
