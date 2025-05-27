from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    listaJogos = ['The Legend of Zelda',
                  'Super Mario Bros', 'Metroid', 'Donkey']
    return render_template('Lista.html', titulo='Jogos', jogos=listaJogos)


app.run()
