from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Articles(db.Model):
    id = Column(Integer, primary_key=True)
    article = Column(String(128))
    __searchable__ = []
    
    def to_json(self):
        return dict(id=self.id, article=self.article)

    def __repr__(self):
        return '{}'.format(self.article)