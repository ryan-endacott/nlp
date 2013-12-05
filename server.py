import os
from flask import Flask, render_template
#from summary import summarize

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
  return render_template('index.html')
