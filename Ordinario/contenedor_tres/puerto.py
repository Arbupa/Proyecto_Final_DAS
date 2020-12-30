import time
from scraper import *
from interface import *
from anime_search_db import *
from animebyid_db import *
from genre_anime_db import *
from manga_search_db import *

class InsertaDatos(DbInterface):
    # def __init__(self) -> None:
    #     self.scrap = Scraper()
    #     self.db_anime_search = DbAnimeSearch()

############################### ANIME BY SEARCH ###############################
    def create_tables(self):
        # db_anime_search = DbAnimeSearch()
        # db_anime_search.create_tab_animebysearch()
        # db_anime_id = DbAnimeById()
        # db_anime_id.create_tab_animebyid()
        # db_manga = DbManga()
        # db_manga.create_tab_mangabysearch()
        db_anime_genre = DbAnimeByGenre()
        db_anime_genre.create_tab_animebygenre()

    def inserta_data_anime_search(self):
        scrap = Scraper()
        animedetailsname = scrap.animedetailsname()
        db_anime_search = DbAnimeSearch()
        print("la lista es: ")
        print(animedetailsname)
        #time.sleep(10)
        return db_anime_search.insert_animebysearch(animedetailsname)
############################### ANIME BY SEARCH ###############################

############################### ANIME BY ID ###############################
    def inserta_data_anime_by_id(self):
        scrap = Scraper()
        anime_details = scrap.animedetailsid()
        db_anime_search = DbAnimeById()
        print("la lista por id es: ")
        print(anime_details)
        return db_anime_search.insert_animebyid(anime_details)

############################### ANIME BY ID ###############################
    def insert_data_genre_anime(self):
        scrap = Scraper()
        anime_details = scrap.animeforgenreid()
        db_anime_search = DbAnimeByGenre()
        #print("la lista por id es: ")
        #print(anime_details)
        return db_anime_search.insert_animebygenre(anime_details)


    def insert_data_manga_search(self):
        scrap = Scraper()
        anime_details = scrap.mangaforname()
        db_anime_search = DbManga()
        #print("la lista por id es: ")
        #print(anime_details)
        return db_anime_search.insert_mangabysearch(anime_details)

if __name__ == "__main__":
    #time.sleep(9)
    crea_datos_db = InsertaDatos()
    crea_datos_db.create_tables()
    # crea_datos_db.inserta_data_anime_search()
    # time.sleep(4)
    # crea_datos_db.inserta_data_anime_by_id()
    #meter un sleep
    #crea_datos_db.insert_data_manga_search()
    #crea_datos_db.insert_data_genre_anime()
    #Hasta aqui funciona :D

    #AHORA CORRER TODOO METIENDO SLEEPS
    #TAMBIEN AGREGAR UNA POSIBLE CONSULTA
    #EN UN IF PARA EVITAR QUE AL VOLVERLO 
    #A CORRER ESTE DE ERROR CON LAS TABLAS 
    #E INSERTS