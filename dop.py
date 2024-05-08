from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE)URI'] = 'sqlite:///registro.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PrimeiroNome = db.Column(db.String(100))
    SegundoNome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

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
        novo_usuario = Usuario(PrimeiroNome=Pnome, SegundoNome=Snome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return f'Obrigado por se registrar, {Pnome} {Snome}!'

    return render_template('registro.html')

if __name__ == '__main__':
    db.create_all()
    app.run () 