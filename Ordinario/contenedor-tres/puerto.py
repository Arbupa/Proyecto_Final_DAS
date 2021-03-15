import time
from scraper import *
from interface import *
from dbinteraction import *

# time.sleep(30)


class InsertaDatos(DbInterface):

    def create_tables(self):
        db_interact = DbInteraction()
        db_interact.create_tab_animebygenre()
        db_interact.create_tab_animebysearch()
        db_interact.create_tab_animebyid()
        db_interact.create_tab_mangabysearch()

    def insert_data_anime_search(self):
        scrap = Scraper()
        animes_to_search = ["shingeki no kyojin", "pokemon", "boku no hero",
                            "code geass", "hunter x hunter", "shokugeki no souma"]
        anime_by_name = scrap.anime_by_name(animes_to_search)
        db_interact = DbInteraction()
        return db_interact.insert_animebysearch(anime_by_name)

    def insert_data_anime_by_id(self):
        scrap = Scraper()
        id_anime = [num for num in range(1, 100)]
        anime_details = scrap.anime_by_id(id_anime)
        db_interact = DbInteraction()
        return db_interact.insert_animebyid(anime_details)

    def insert_data_genre_anime(self):
        scrap = Scraper()
        lista_ids = [num for num in range(1, 21)]
        anime_details = scrap.anime_by_genre_id(lista_ids)
        db_interact = DbInteraction()
        return db_interact.insert_animebygenre(anime_details)

    def insert_data_manga_search(self):
        scrap = Scraper()
        mangas = ["kimetsu no yaiba", "berserk",
                  "one piece", "dragon ball", "saint seiya"]
        manga_details = scrap.manga_by_name(mangas)
        db_interact = DbInteraction()
        return db_interact.insert_mangabysearch(manga_details)


if __name__ == '__main__':
    db_interact = DbInteraction()
    # Check if data exists inside database,
    # if don't, create tables and inserts.
    var = db_interact.db_data_exists()
    if (var == False):
        create_data_db = InsertaDatos()
        create_data_db.create_tables()
        print("Creating data...")
        print(create_data_db.insert_data_anime_search())
        time.sleep(4)
        print("inserting all data...")
        print(create_data_db.insert_data_anime_by_id())
        time.sleep(12)
        print(create_data_db.insert_data_manga_search())
        time.sleep(12)
        print(create_data_db.insert_data_genre_anime())
