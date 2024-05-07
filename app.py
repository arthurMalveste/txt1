from flask import Flask, jsonify
from funcoes import maior_de_50
from random_data import *
from funcoes import *


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Arthur Miele Malveste"})

from api import bp
app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0")