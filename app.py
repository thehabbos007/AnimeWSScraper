from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from scrape import WeebMachine
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/show', methods=['POST'])
def getList():
    if request.method == 'POST':

        data = WeebMachine(str(request.form['show']))
        resp = jsonify({"list": data, "status": 200})

        return resp

if __name__ == "__main__":
    app.run()