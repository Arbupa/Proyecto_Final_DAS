from scraper import *
from anime_search_db import *
from interface import *

class InsertaDatos(DbInterface):
    # def __init__(self) -> None:
    #     self.scrap = Scraper()
    #     self.db_anime_search = DbAnimeSearch()

############################### ANIME BY SEARCH ###############################
    def create_table(self):
        db_anime_search = DbAnimeSearch()
        return db_anime_search.create_tab_animebysearch()

    def insert_data(self):
        scrap = Scraper()
        animedetaillsname = scrap.animedetaillsname()
        db_anime_search = DbAnimeSearch()
        print("la lista es: ")
        print(animedetaillsname)
        return db_anime_search.insert_animebysearch(animedetaillsname)
############################### ANIME BY SEARCH ###############################

############################### ANIME BY SEARCH ###############################
    def create_table(self):
        db_anime_search = DbAnimeSearch()
        return db_anime_search.create_tab_animebysearch()

    def insert_data(self):
        scrap = Scraper()
        animedetaillsname = scrap.animedetaillsname()
        db_anime_search = DbAnimeSearch()
        print("la lista es: ")
        print(animedetaillsname)
        return db_anime_search.insert_animebysearch(animedetaillsname)



if __name__ == "__main__":
    crea_datos_db = InsertaDatos()
    crea_datos_db.create_table()
    crea_datos_db.insert_data()
    # InsertaDatos.create_table()
    # InsertaDatos.insert_data()