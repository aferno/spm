from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from controllers import article, articles

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
api = Api(app)
db=SQLAlchemy(app)
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = db
    return db

api.add_resource(articles, "/articles", "/GET")
api.add_resource(article, "/article/<int:articleId>", "/GET", "/POST", "/DELETE")

if __name__ == "__main__":
    app.run()