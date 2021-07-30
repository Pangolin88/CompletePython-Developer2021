from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/<username>')
def hello_world(username=None):
    return render_template('hello.html', name=username)

@app.route('/blogs')
def blogs():
    return 'This is all my blogs'

@app.route('/about')
def about():
    return render_template('about.html')




