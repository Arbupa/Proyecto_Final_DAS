from base_alchemy import *
from models import *

class AnimeGenreApi():

    #checar flask.views.MethodView para cambiar estas funciones
    def show_genre_by_id(self, id: int):
        query_response = session.query(AnimeByGenre).get(id)
        if query_response == None:
            return print("ID not found")
            
        print(query_response.title, query_response.episodes, query_response.image_url)
        print(type(query_response))
        session.close()
        return query_response

    def insert_genre_by_id(self, lista: list):
        pass

    def update_genre_by_id(self, id: int):
        pass

    def delete_genre_by_id(self, id:int):
        pass


db = AnimeGenreApi()
#lista = [{}]
db.show_genre_by_id(110)