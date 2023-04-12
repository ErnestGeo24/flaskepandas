from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=";")
    
@app.route('/')
def home():
    lingua_film = dati_film.drop_duplicates(subset=['Language'])
    return render_template('search4.html', lingue= list(lingua_film['Language']))

@app.route('/search', methods = ['POST'])
def search():
    film = request.form.getlist("film")
    risultato = pd.DataFrame()
    for lingua in film:
        data = dati_film[dati_film['Language'].str.contains(lingua)]
        risultato = pd.concat([risultato, data])
    if len(risultato) == 0:
        table = 'Lingua non trovata'
    else:
        table = risultato.to_html()
    return render_template('table.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)