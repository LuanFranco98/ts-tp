from logging import debug
from flask import Flask , render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)