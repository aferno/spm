from flask import Flask
from flask_restful import Api

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    api = Api(app)

    from .models import db
    db.init_app(app)

    api = Api(app)

    from .controllers import article, articles
    api.add_resource(articles, "/articles", "/GET")
    api.add_resource(article, "/article/<int:articleId>", "/GET", "/POST", "/DELETE")

    return app