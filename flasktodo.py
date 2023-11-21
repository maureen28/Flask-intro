from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_migrate import Migrate

app = Flask(__name__)

# setting a secret key
app.config['SECRET_KEY'] = '9cfdfea1bb00aa76d0c4ea31410ae42f'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfuly for {form.username.data} :)')
        
        return redirect(url_for('home'))
    return render_template('register.html', form = form, title='Register')

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f'Login successful for {form.email.data} :)')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful')
            
    return render_template('login.html', form = form, title='Login')


if __name__ == '__main__':
        app.run(debug=True)