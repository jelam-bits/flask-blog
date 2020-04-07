from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
#FLASK_APP = "flaskblog.py"
app = Flask(__name__)
app.config['SECRET_KEY'] = '041440ca94069ec41f4e7a2ca09a49c33b861baf5beb5e4622eeee844807944268b351656d9ae70f81d0162e0f666738c60bba5c7064c92ba29d7fa4c8f0cb17562e071831bf379c041117146e4ae0bf9e4a2c1a600ef08eb2f096beac6f10e856e8ddda98cb5b6b0a8303aea07a2b42ba007df3a698b697c01e7c773480a4c23bff52897854bff9cb99e12c50037c6cc8a65ab31e0d36e672bdad878b7915a6f8315a9b7aaf91be399a4f1a9060e218450e4e548c14332b974aff60b2b4ff8e0aed94c2f508369cde0902ab54d26b2d4da8c06d7360164799aaeb160e2f35055d2e61b9c7c321e36ff149989abc8582855c0d818ac763211a7bdc3a8e71c71a'

posts = [
    {
        'author': 'Jonathan Elam',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'April 2, 2020'
    },
    {
        'author': 'Alphie McPhee',
        'title': 'Blog Post 2',
        'content': 'Another Cool Post',
        'date_posted': 'April 2, 2020'
    }  
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)