import os
from flask import Flask, render_template, request
from summary import summarize

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    text = request.form.get('text', None)
    if text is None:
      return render_template('index.html', summary="Error, didn't get text to summarize.")
    else:
      length = int(request.form.get('length', 3)) # default length of 3
      s = summarize(request.form.get('text', None), raw=True, length=length)
      return render_template('index.html', summary=s, text=text)

  return render_template('index.html')
