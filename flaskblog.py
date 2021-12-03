from logging import debug
from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] =  'e081d5432db867734e0ae997957873db'

posts = [
    {
        'author': 'Luan Franco',
        'title' : 'Blog Post 1',
        'content' : 'Content 1',
        'date_posted' :'Dez, 2 , 2021'
    },
    {
        'author': 'Arthur Franco',
        'title' : 'Blog Post 2',
        'content' : 'Content 2',
        'date_posted' :'Dez, 3 , 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'teste@teste.com' and form.password.data == 'senha':
            flash('You have been logged in!', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check email and password', 'dangerous')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)