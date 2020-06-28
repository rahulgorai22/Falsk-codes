from flask import Flask, render_template
from flask.json import jsonify
app = Flask(__name__)

@app.route("/employee")
def sendData():
    data = [
        {
           "firstname":"Rahul",
           "lastname":"Gorai" 
        },
        {
           "firstname":"Sumit",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Kunal",
           "lastname":"Bhai" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        },
        {
           "firstname":"Prince",
           "lastname":"Kumar" 
        }
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True,port=5001)