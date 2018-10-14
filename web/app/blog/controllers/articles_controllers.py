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
    def post(self, articleId):
        article = Articles(title = 'This is first article', article = '<h1>Lorem ipsum dolor sit amet</h1>, <p>consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>')
        db.session.add(article)
        db.session.commit()
        return 'Done!'
    def delete(self, articleId):
        article = Articles.query.filter_by(id=articleId).one()
        db.session.delete(article)
        db.session.commit()
        return 'Deleted'
