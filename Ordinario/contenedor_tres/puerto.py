import time
from scraper import *
from interface import *
from anime_search_db import *
from animebyid_db import *
from genre_anime_db import *
from manga_search_db import *

class InsertaDatos(DbInterface):
    
    def create_tables(self):
        db_anime_genre = DbAnimeByGenre()
        db_anime_genre.create_tab_animebygenre()
        db_anime_search = DbAnimeSearch()
        db_anime_search.create_tab_animebysearch()
        db_anime_id = DbAnimeById()
        db_anime_id.create_tab_animebyid()
        db_manga = DbManga()
        db_manga.create_tab_mangabysearch()
        
    def inserta_data_anime_search(self):
        scrap = Scraper()
        animedetailsname = scrap.animedetailsname()
        db_anime_search = DbAnimeSearch()
        #print("la lista es: ")
        #print(animedetailsname)
        return db_anime_search.insert_animebysearch(animedetailsname)

    def inserta_data_anime_by_id(self):
        scrap = Scraper()
        anime_details = scrap.animedetailsid()
        db_anime_search = DbAnimeById()
        #print("la lista por id es: ")
        #print(anime_details)
        return db_anime_search.insert_animebyid(anime_details)

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
    # compruebo si la data existe dentro de una tabla, 
    # y si no, la creo
    db_anime_genre = DbAnimeByGenre()
    var = db_anime_genre.db_data_exists()
    if (var == False): 
        crea_datos_db = InsertaDatos()
        crea_datos_db.create_tables()
        crea_datos_db.inserta_data_anime_search()
        time.sleep(4)
        crea_datos_db.inserta_data_anime_by_id()
        time.sleep(12)
        crea_datos_db.insert_data_manga_search()
        time.sleep(12)
        crea_datos_db.insert_data_genre_anime()
    else:
        pass
    #Hasta aqui funciona :D
