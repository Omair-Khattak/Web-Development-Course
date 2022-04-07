from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user = json.loads(response.text)
    
    for i in range (len(user)):
        uId = "userId"
        uId_values = [a_dict[uId] for a_dict in user]
    
        id = "id"
        id_values = [a_dict[id] for a_dict in user]
    
        title = "title"
        title_values = [a_dict[title] for a_dict in user]
    
        completed = "completed"
        comp_values = [a_dict[completed] for a_dict in user]
    
    return render_template("index.html", user=user, len = len(user), uId_values = uId_values,
                    id_values=id_values, title_values=title_values,comp_values=comp_values)

if __name__ == '__main__':
    app.run()