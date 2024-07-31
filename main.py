from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
   user_list = [{'username': 'John', 'age': 30, 'city': 'New', 'state': 'California', 'country': 'USA'},{'username': 'Jane', 'age': 25, 'city': 'Boston', 'state': 'Massachusetts', 'country': 'USA'},{'username': 'Bob', 'age': 40, 'city': 'Seattle', 'state': 'Washington', 'country': 'USA'}]
   return render_template('index.html',user_list=user_list)





app.run(debug=True)