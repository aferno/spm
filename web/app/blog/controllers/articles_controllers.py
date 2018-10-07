from flask_restful import Resource
from ..models import Articles, db

class articles(Resource):
    def get(self):
        all_articles = Articles.query.all()
        return [one_article.to_json() for one_article in all_articles]

class article(Resource):
    def get(self, articleId):
        article = Articles.query.get(articleId)
        return article.to_json()
        #return "Yeee it works article"
    def post(self, articleId):
        article = Articles(article = 'Body')
        db.session.add(article)
        db.session.commit()
        return "Done!"
    def delete(self, articleId):
        article = Articles.query.filter_by(id=articleId).one()
        db.session.delete(article)
        db.session.commit()
        return "Deleted"
