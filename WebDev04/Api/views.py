from flask import abort, render_template
from flask import jsonify
from flask import request,make_response, render_template

from Api import app
from .models import TodoList, TodoListSchema, db

todo_item_schema = TodoListSchema()
todo_list_schema = TodoListSchema(many=True)

@app.route("/")
def index():
    data = TodoList.query.all()
    return render_template('ajax.html', data=data)

@app.route("/todo/api", methods=["POST"])
def add_item():
    """endpoint to create new todo_item"""
    if 'title' in request.form and 'description' in request.form:
        title = request.form['title']
        description = request.form['description']

        todo_item = TodoList(title, description)
        db.session.add(todo_item)
        db.session.commit()
        return todo_item_schema.jsonify(todo_item)
    abort(400)


@app.route("/todo/api", methods=["GET"])
def get_todo_list():
    """endpoint to show all todo items"""
    result = TodoList.query.all()
    result = todo_list_schema.dump(result)
    return jsonify(result)


@app.route("/todo/api/<id>", methods=["GET"])
def get_todo_item(id):
    """endpoint to get todo_item detail by id"""
    get_todo = TodoList.query.get(id)
    todo_schema = TodoListSchema()
    todo = todo_schema.dump(get_todo)
    return make_response(jsonify({"todo": todo}))

@app.route('/todo/api/<id>', methods=['PUT'])
def update_todo_by_id(id):
    update = TodoList.query.get(id)
    title = request.form['title']
    description = request.form['description']

    update.title = title
    update.description = description

    db.session.commit()
    return todo_item_schema.jsonify(update)

@app.route('/todo/api/<id>', methods=['DELETE'])
def delete_todo_by_id(id):
   get_todo = TodoList.query.get(id)
   db.session.delete(get_todo)
   db.session.commit()
   return make_response("", 204)
