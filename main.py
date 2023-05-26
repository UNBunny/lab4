
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def check_credentials(username, password):
    # Проверяем логин и пароль
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                return True
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('home'))
        else:
            error = 'Неправильный логин или пароль!'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return "Добро пожаловать на сайт!"

if __name__ == '__main__':
    app.run()