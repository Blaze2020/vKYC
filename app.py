from flask import Flask, render_template, request, flash, redirect, url_for, session
from hashlib import md5

from blockchain.BlockChain import BlockChain
from middleware.dboperations import insert_data, fetch_data
from middleware.middlewareoperations import extractname, proccessdata
from datetime import timedelta

# from blockchain import BlockChain, Block

app = Flask(__name__)

# To set a secret key
app.secret_key = '3cdbce4e-afa4-49c6-ba6a-44f2b42e642c'
# Setting Session Time
app.permanent_session_lifetime = timedelta(minutes=100)
# initialize Blockchain
blockchain = BlockChain()


# Data

# Data = [{
#     'Name': 'Karanam Kalpesh',
#     'Profession': 'Software Developer',
#     'Age': 23,
#     'Aim': 'To establish a game development Company'
# }]


@app.route('/')
def index_html():  # put application's code here
    return render_template('index.html')


# Register
@app.route('/register', methods=['POST'])
def register():
    message = ''
    if request.method == 'POST' and request.form.get('password') == request.form.get('checkpassword'):
        email = request.form.get('username').strip()
        password = request.form.get('password').strip()
        checkpassword = request.form.get('checkpassword').strip()
        # Hashing using md5
        hash_value = md5(password.encode())
        insert_data(email, hash_value.hexdigest())
        print(hash_value.hexdigest())
        print("Registration Success")
        print(email, password, checkpassword)
        return redirect(url_for('index_html'))
    else:
        print('Registration Fail, try again')
        return render_template('index.html')


# Login
@app.route('/login', methods=['POST'])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form.get('username').strip()
        password = request.form.get('password').strip()
        print(email, password)
        # Hashing using md5
        hash_value = md5(password.encode())
        # print(hash_value.hexdigest())
        if fetch_data(email, hash_value.hexdigest()):
            # Creating Session
            session.permanent = True
            session['user'] = email
            # print("Login Success")
            return redirect(url_for('profile'))
        else:
            if 'user' in session:
                # print('Login Fail, try again')
                return redirect(url_for('profile'))
            return render_template('index.html')


# Profile Page
@app.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        return render_template('home.html', message=extractname(user))
    else:
        return redirect(url_for('index_html'))


@app.route('/userData', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        if proccessdata(blockchain, request.form):
            return redirect(url_for('about'))
        else:
            return redirect(url_for('profile'))
    else:
        return render_template('home.html')


# logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index_html'))


@app.route('/about')
def about():
    return render_template('about.html', message='Success')


if __name__ == '__main__':
    app.run(debug=True)
