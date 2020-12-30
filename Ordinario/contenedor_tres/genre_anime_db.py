import mysql.connector
from mysql.connector import cursor
import time
class DbAnimeByGenre():

    def __init__(self):
        self.mydb = mysql.connector.connect(
                        host="localhost",
                        user="invitao",
                        password="secret123",
                        database="app_db"
                        )
    
        self.mycursor = self.mydb.cursor()


    def create_tab_animebygenre(self):
      query_table = """CREATE TABLE animebygenre ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  id_genre Int, page_id Int, title varchar(150),image_url varchar(200), episodes varchar(20), airing varchar(20),
                  type varchar(20), start_date varchar(50), end_date varchar(50),
                  members varchar(20), rated varchar(10)
                  );"""

      if self.mycursor.execute(query_table):
          print("se creó la db")
      else:
          print("La tabla ya existe")
    #   self.mycursor.execute("SHOW TABLES")
    #   for x in self.mycursor:
    #     print(x)

    def insert_animebygenre(self, lista: list):
        print("La lista que recibe la db es:")
        print(lista)
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
        return "se insertaron"

    def show_tab_animebygenre(self):
        query = ("SELECT * FROM animebygenre;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)

#db = DbAnimeByGenre()
#db.create_tab_animebygenre()
#db.insert_animebygenre()
#db.show_tab_animebygenre()
