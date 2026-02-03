import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home/<name>")
def home_route(name):
    url=f"https://api.agify.io/?name={name}"
    response=requests.get(url,verify=False)
    age=response.json()['age']
    return render_template("index.html", name=name, age=age)

if __name__=="__main__":
   app.run(host="127.0.0.1", port=8000, debug=True)