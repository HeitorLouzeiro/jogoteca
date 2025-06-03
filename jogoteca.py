from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.console}'


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo('The Legend of Zelda', 'Aventura', 'NES')
    jogo2 = Jogo('Super Mario Bros', 'Plataforma', 'NES')
    jogo3 = Jogo('Metroid', 'Aventura', 'NES')

    listaJogos = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


app.run()
