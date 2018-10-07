from sqlalchemy import Column, Integer, String
#from app import db
from werkzeug.local import LocalProxy

db = LocalProxy(get_db)

class Articles(db.Model):
    id = Column(Integer, primary_key=True)
    article = Column(String(128))
    
    def to_json(self):
        return dict(id=self.id, article=self.article)

    def __repr__(self):
        return '{}'.format(self.article)