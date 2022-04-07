from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from Api import app

db = SQLAlchemy(app)
ma = Marshmallow(app)


class TodoList(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(120))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, description):
        # self.id = id
        self.title = title
        self.description = description
        
    def __repr__(self):
        return f"{self.id}"


class TodoListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


db.create_all()
