from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify([
        {
            "id": "0",
            "time": "00:00",
            "program": "Morning News",
            "description":"In other news"
        },
        {
            "id": "1",
            "time": "01:00",
            "program": "Current Affairs",
            "description":"Its all up in flames"
        },
        {
            "id": "2",
            "time": "01:05",
            "program": "Bluey!",
            "description":"Yaay!"
        },
    ])

if __name__ == '__main__':
    app.run(debug=True)