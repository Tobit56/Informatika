from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def article():
    cislo = random.randint(1, 10)
    return render_template("html.html", cislo = cislo)
    
