from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Nastavit adresář pro nahrávané soubory
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Zajistit existenci adresáře pro nahrávané soubory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Seznam pro ukládání dat (pro jednoduchost použijeme globální proměnnou)
saved_data = []

@app.route("/")
def article():
    cislo = random.randint(1, 10)
    # Získat názvy nahraných obrázků (pokud existují)
    image_filenames = request.args.getlist('image_filenames')
    return render_template("html.html", cislo=cislo, image_filenames=image_filenames, saved_data=saved_data)

@app.route("/upload", methods=["POST"])
def upload():
    if 'files' not in request.files:
        return "No files part"

    files = request.files.getlist('files')

    filenames = []
    for file in files:
        if file.filename == '':
            continue

        # Uložit nahraný obrázek do adresáře pro nahrávané soubory
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        filenames.append(file.filename)

    # Přesměrovat na domovskou stránku s názvy nahraných obrázků a uloženými daty
    return redirect(url_for('article', image_filenames=filenames, saved_data=saved_data))

@app.route("/add_data", methods=["POST"])
def add_data():
    # Získat data z formuláře
    name = request.form.get('name')
    message = request.form.get('message')

    # Uložit data do seznamu
    saved_data.append({'name': name, 'message': message})

    # Přesměrovat na domovskou stránku s uloženými daty
    return redirect(url_for('article', saved_data=saved_data))

if __name__ == "__main__":
    app.run(debug=True)
