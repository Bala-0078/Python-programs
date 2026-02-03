import requests
from flask import Flask, render_template

app = Flask(__name__)

API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

def get_posts():
    response = requests.get(API_URL, timeout=10,verify=False)
    response.raise_for_status()
    return response.json()

@app.route("/home")
def get_all_posts():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    posts = get_posts()
    requested_post = next((p for p in posts if p["id"] == index), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)