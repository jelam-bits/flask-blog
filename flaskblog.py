from flask import Flask, render_template
#FLASK_APP = "flaskblog.py"
app = Flask(__name__)

posts = [
    {
        'author': 'Jonathan Elam',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'April 2, 2020'
    },
    {
        'aufthor': 'Alphie McPhee',
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

if __name__ == '__main__':
    app.run(debug=True)