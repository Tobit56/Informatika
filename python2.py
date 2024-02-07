from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Nastavit adresář pro nahrávané soubory
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Zajistit existenci adresáře pro nahrávané soubory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def article():
    cislo = random.randint(1, 10)
    # Získat název nahraného obrázku (pokud existuje)
    image_filename = request.args.get('image_filename')
    return render_template("chat.html", cislo=cislo, image_filename=image_filename)

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        # Uložit nahraný obrázek do adresáře pro nahrávané soubory
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        # Přesměrovat na domovskou stránku s názvem nahraného obrázku
        return redirect(url_for('article', image_filename=file.filename))

if __name__ == "__main__":
    app.run(debug=True)
