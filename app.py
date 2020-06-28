from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route("/home")
def home():
    # name = "Rahul"
    data = requests.get("http://127.0.0.1:5001/employee")
    print(data.text)
    return render_template("index.html", employees = json.loads(data.text))
    
if __name__ == "__main__":
    app.run(debug=True)