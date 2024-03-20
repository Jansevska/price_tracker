from app import app
from flask import render_template

@app.route('/')
def index():
    # iPad data from sqlite3
    return render_template('index.html')

