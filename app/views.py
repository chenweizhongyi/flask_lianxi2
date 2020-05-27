from app import app
from flask import render_template
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'chenwei'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',form = form)