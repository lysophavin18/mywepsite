from flask import Flask, render_template

app = Flask(__name__)

COURSES = [{
    'id': 1,
    'name school': "បឋមសិក្សា ព្រែកចាម,Prek Cham Primary School ",
    'Location': "77MX+8W, អ្នកលឿង",
    'Year': '2009-2015'
}, {
    'id': 2,
    'name school': "អនុវិទ្យាល័យបន្លិចប្រាសាទ,Secondary Banlich Prasat ",
    'Location':
    "8M2+C6, អ្នកលឿង",
    'Year': '2016-2018'
}, {
    'id': 3,
    'name school': "វិទ្យាល័យពាមរក៍, Peam Ro High School",
    'Location':
    "875J+JHH, ផ្លូវជាតិលេខ ១១, ពាមរក៍",
    'Year': '2019-2021'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', courses=COURSES)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
