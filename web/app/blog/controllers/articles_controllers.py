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
        article = Articles(title = 'Крутой поиск на сайте', article = '<h1>Примерную схему работы конвейера можно увидеть на картинке поблизости. Анализ начинается с опциональных символьных фильтров</h1>,'
        + '<p> Полученный результат передается токенизатору, главному и единственному обязательному элементу анализатора. Здесь предложение очищается от знаков препинания, разбивается на отдельные слова-токены, которые могут либо сохранять имеющуюся форму, либо обрезаться только до основы слова, либо обрабатываться еще каким-либо образом в зависимости от токенизатора.</p>')
        db.session.add(article)
        db.session.commit()
        return 'Done!'
    def delete(self, articleId):
        article = Articles.query.filter_by(id=articleId).one()
        db.session.delete(article)
        db.session.commit()
        return 'Deleted'
