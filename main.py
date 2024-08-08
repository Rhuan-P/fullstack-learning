from flask import Flask, render_template, request, jsonify, url_for, redirect
from db.db import products

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html', products=products)

@app.route("/register" , methods=["POST"])
def register():
    product = {'id': len(products) +1, **request.form}
    products.append(product)
    return redirect(url_for('index'))

@app.route("/delete_product/<int:id>", methods=["DELETE"])
def delete_product(id):
    
    return (request.form)






app.run(debug=True)