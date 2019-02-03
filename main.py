from flask import Flask
import random, sqlite3

app = Flask(__name__)

@app.route('/')
