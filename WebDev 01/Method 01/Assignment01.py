from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user = json.loads(response.text)
    return render_template("index.html", user=user, len = len(user))

if __name__ == '__main__':
    app.run()