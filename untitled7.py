# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lZ4zozSLhNsj5gKsjLpg8bmhJEqy69pK
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
