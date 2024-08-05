from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # products whith name,price, validity =  valid or expired
    products = [
        {"name": "Apple", "price": 10, "validity": "valid"},
        {"name": "Orange", "price": 20, "validity": "valid"},
        {"name": "Banana", "price": 30, "validity": "expired"},
        {"name": "Mango", "price": 40, "validity": "valid"},
        {"name": "Pineapple", "price": 50, "validity": "expired"},
        {"name": "Watermelon", "price": 60, "validity": "valid"},
        {"name": "Grapes", "price": 70, "validity": "expired"},

    ]
   
    
   
    

    
    return render_template('index.html', products=products)

app.run(debug=True)