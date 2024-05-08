from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        Pnome = request.form['PrimeiroNome']
        Snome = request.form['SegundoNome']
        email = request.form['email']
        senha = request.form['senha']
        return f'Obrigado por se registrar, {Pnome} {Snome}!'

    return render_template('registro.html')

if __name__ == '__main__':
    app.run ()