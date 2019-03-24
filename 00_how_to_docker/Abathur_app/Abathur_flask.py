#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
    <head>
    <title>#Siniikit</title>
    </head>
    <body>
    <h1>Hello, World</h1>
    </body>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)
