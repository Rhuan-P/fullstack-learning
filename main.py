from flask import Flask, render_template
from db.db import products

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html', products=products)
app.run(debug=True)