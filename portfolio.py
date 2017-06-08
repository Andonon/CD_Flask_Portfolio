'''Flask "portfolio" assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('portfolio.html')

@app.route('/projects')

def projects():
    return render_template('projects.html')

@app.route('/about')

def about():
    return render_template('about.html')

app.run(debug=True)
