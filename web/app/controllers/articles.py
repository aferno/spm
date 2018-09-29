from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

articles = { "title": "Все статьи",  "msg": "Как правильно делать то или иное" }
article = { "title": "Статья №",  "msg": "Заголовок статьи" }

class Articles(Resource):
    def get(self):
        return articles
    def post(self):
        return "Data from POST"


class Article(Resource):
    def get(self):
        return article
    def post(self):
        #return json.dumps(hlw1)
        return "Data from POST"


api.add_resource(Articles, "/articles")
api.add_resource(Article, "/article")
