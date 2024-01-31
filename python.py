from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def article():
    return render_template("html.html")
