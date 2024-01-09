from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # validar username e password
        if username == 'user' and password == 'pass':
            return 'Login realizado com sucesso!'
        else:
            return 'Nome de usuario ou senha incorretos'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

