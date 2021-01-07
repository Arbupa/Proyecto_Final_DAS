import time
from scraper import *
from interface import *
from dbinteraction import *

class InsertaDatos(DbInterface):
    
    def create_tables(self):
        db_interact = DbInteraction()
        db_interact.create_tab_animebygenre()
        db_interact.create_tab_animebysearch()
        db_interact.create_tab_animebyid()
        db_interact.create_tab_mangabysearch()
        
    def inserta_data_anime_search(self):
        scrap = Scraper()
        animedetailsname = scrap.animedetailsname()
        db_interact = DbInteraction()
        return db_interact.insert_animebysearch(animedetailsname)

    def inserta_data_anime_by_id(self):
        scrap = Scraper()
        anime_details = scrap.animedetailsid()
        db_interact = DbInteraction()
        return db_interact.insert_animebyid(anime_details)

    def insert_data_genre_anime(self):
        scrap = Scraper()
        anime_details = scrap.animeforgenreid()
        db_interact = DbInteraction()
        return db_interact.insert_animebygenre(anime_details)

    def insert_data_manga_search(self):
        scrap = Scraper()
        anime_details = scrap.mangaforname()
        db_interact = DbInteraction()
        return db_interact.insert_mangabysearch(anime_details)

if __name__ == "__main__":
    #time.sleep(9)
    # compruebo si la data existe dentro de una tabla, 
    # y si no, la creo
    db_interact = DbInteraction()
    var = db_interact.db_data_exists()
    if (var == False): 
        crea_datos_db = InsertaDatos()
        crea_datos_db.create_tables()
        # crea_datos_db.inserta_data_anime_search()
        # time.sleep(4)
        # crea_datos_db.inserta_data_anime_by_id()
        # time.sleep(12)
        # crea_datos_db.insert_data_manga_search()
        # time.sleep(12)
        crea_datos_db.insert_data_genre_anime()
    else:
        pass
    #Hasta aqui funciona :D
