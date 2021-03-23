import mysql.connector
from mysql.connector import cursor
import time


class DbInteraction():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="invitao",
            password="secret123",
            database="app_db"
        )

        self.mycursor = self.mydb.cursor()

    def create_tab_animebysearch(self):
        query_table = """CREATE TABLE animebysearch (id Int NOT NULL AUTO_INCREMENT,
                  page_id Int, title varchar(150), episodes varchar(20), type varchar(20),
                  rated varchar(20), image_url varchar(200), score varchar(20), synopsis varchar(5000),
                  airing varchar(50), members varchar(20), PRIMARY KEY (id)
                  );"""
        try:
            self.mycursor.execute(query_table)
            return "the table was created"
        except:
            return "the table was not created"

    def insert_animebysearch(self, lista):
        for i in lista:
            synopsis = i["synopsis"]
            synopsis = synopsis.replace("'", "")
            query = f"INSERT INTO animebysearch (page_id, title, episodes, type, rated, image_url, score, synopsis, airing, members) VALUES ('{i['page_id']}','{i['title']}','{i['episodes']}','{i['type']}','{i['rated']}','{i['image_url']}','{i['score']}','{synopsis}','{i['airing']}','{i['members']}');"
            self.mycursor.execute(query)
            self.mydb.commit()
        return "Data inserted 1/4..."

    def create_tab_animebygenre(self):
        query_table = """CREATE TABLE animebygenre ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  id_genre Int, page_id Int, title varchar(150),image_url varchar(200), episodes varchar(20), airing varchar(20),
                  type varchar(20), start_date varchar(50), end_date varchar(50),
                  members varchar(20), rated varchar(10)
                  );"""

        self.mycursor.execute(query_table)

    def insert_animebygenre(self, lista: list):
        cont = 1
        for i in lista:
            if cont == 25:
                time.sleep(3)
                cont = 1

            title = i["title"]
            title = title.replace("'", "")
            query = f"INSERT INTO animebygenre (id_genre, page_id, title, image_url, episodes, airing, type, start_date, end_date, members, rated) VALUES ('{i['id_genre']}','{i['page_id']}','{title}','{i['image_url']}','{i['episodes']}','{i['airing']}','{i['type']}','{i['start_date']}','{i['end_date']}','{i['members']}','{i['rated']}');"
            self.mycursor.execute(query)
            self.mydb.commit()
            cont += 1

        return "All data inserted succesfully 4/4"

    def db_data_exists(self):
        query = "SELECT EXISTS(SELECT * FROM animebygenre WHERE id = 1);"
        exists = False
        try:
            self.mycursor.execute(query)
            print("Ya existen datos")
            exists = True
        except:
            print("No existen datos :c")
        return exists

    def create_tab_animebyid(self):
        query_table = """CREATE TABLE animebyid (id Int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  page_id Int, image_url varchar(150), title varchar(200), episodes varchar(20), status varchar(75),
                  score varchar(20), rank varchar(20), duration varchar(50), synopsis varchar(5000),
                  premiered varchar(50), broadcast varchar(80)
                  );"""

        self.mycursor.execute(query_table)

    def insert_animebyid(self, lista):
        for i in lista:
            title1 = i["title"]
            title2 = title1.replace("'", "")
            title = title2.replace('"', '')
            syno6 = i["synopsis"]
            #synopsis = synopsis.translate({ord('"'): ''})
            syno1 = syno6.replace("'", "")
            synopsis = syno1.replace('"', '')
            query = f"INSERT INTO animebyid (page_id, image_url, title, episodes, status, score, rank, duration, synopsis, premiered, broadcast) VALUES ('{i['page_id']}','{i['image_url']}','{title}','{i['episodes']}','{i['status']}','{i['score']}','{i['rank']}','{i['duration']}','{synopsis}','{i['premiered']}','{i['broadcast']}');"
            self.mycursor.execute(query)
            self.mydb.commit()

        return "Data inserted 2/4..."

    def create_tab_mangabysearch(self):
        query_table = """CREATE TABLE mangabysearch ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    page_id Int, image_url varchar(200),  title varchar(150), publishing varchar(50), type varchar(20),
                    chapters varchar(20), volumes varchar(20), synopsis varchar(5000),
                    start_date varchar(50), end_date varchar(50)
                    );"""

        self.mycursor.execute(query_table)

    def insert_mangabysearch(self, lista: list):
        for i in lista:
            synopsis = i["synopsis"]
            synopsis = synopsis.replace("'", "")
            query = f"INSERT INTO mangabysearch (page_id, image_url, title, publishing, type, chapters, volumes, synopsis, start_date, end_date) VALUES ('{i['page_id']}','{i['image_url']}','{i['title']}','{i['publishing']}','{i['type']}','{i['chapters']}','{i['volumes']}','{synopsis}','{i['start_date']}','{i['end_date']}');"
            self.mycursor.execute(query)
            self.mydb.commit()
        return "Data inserted 3/4..."
