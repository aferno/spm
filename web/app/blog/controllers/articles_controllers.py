from flask_restful import Resource,reqparse
from ..models import Articles, db

parser = reqparse.RequestParser()

class articles(Resource):
    def get(self):
        all_articles = Articles.query.all()
        return [one_article.to_json() for one_article in all_articles]
    def post(self):
        parser.add_argument('title', type=str, help='Title of the article')
        parser.add_argument('article', type=str, help='HTML version of article')
        args = parser.parse_args()
        article = Articles(title = args['title'], article = args['article'])
        db.session.add(article)
        db.session.commit()
        return 201, 'Articles has been created'

class article(Resource):
    def get(self, articleId):
        article = Articles.query.get(articleId)
        return article.to_json()
    
    def delete(self, articleId):
        article = Articles.query.filter_by(id=articleId).one()
        db.session.delete(article)
        db.session.commit()
        return 'Deleted'

    def put(self, articleId):
        parser.add_argument('title', type=str, help='New title of the article')
        parser.add_argument('article', type=str, help='New HTML version of article')
        args = parser.parse_args()
        specArticle = Articles.query.get(articleId)
        specArticle.title = args['title']
        specArticle.article = args['article']
        db.session.add(specArticle)
        db.session.commit()
        return 201, 'Articles has been update'
