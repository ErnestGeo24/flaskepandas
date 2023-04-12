from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=";")
    
@app.route('/')
def home():
    lingua_film = dati_film.drop_duplicates(subset=['Language'])
    return render_template('search3.html', lingue= list(lingua_film['Language'].sort_values("Language")))

@app.route('/search', methods = ['GET'])
def search():
    film = request.args['film']
    risultato = dati_film[dati_film['Language']==film.capitalize()]
    if len(risultato) == 0:
        table = 'Lingua del film non trovata'
    else:
        table = risultato.to_html()
    return render_template('table.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)