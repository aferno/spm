from flask_restful import Resource
from ..models import Articles

class search(Resource):
    def get(self, searchText):
        search, total = Articles.search(searchText, 1, 10)
        return [searched.to_json() for searched in search]
        #total
