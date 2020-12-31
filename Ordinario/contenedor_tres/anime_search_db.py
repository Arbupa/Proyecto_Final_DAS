import mysql.connector
from mysql.connector import cursor

class DbAnimeSearch():
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
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

      self.mycursor.execute(query_table)

    def insert_animebysearch(self, lista):
        for i in lista:
            synopsis = i["synopsis"]
            synopsis = synopsis.replace("'", "") 
            query = f"INSERT INTO animebysearch (page_id, title, episodes, type, rated, image_url, score, synopsis, airing, members) VALUES ('{i['page_id']}','{i['title']}','{i['episodes']}','{i['type']}','{i['rated']}','{i['image_url']}','{i['score']}','{synopsis}','{i['airing']}','{i['members']}');"
            self.mycursor.execute(query)
            self.mydb.commit()
        return "se insertaron"

    def show_animebysearch(self):
        query = ("SELECT * FROM animebysearch;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print(row)

    """query para buscar todas las apariciones de el texto ingresado:
     SELECT * FROM demo 
     WHERE name LIKE '%shingeki no kyojin%';
     OOJOO que cuentan los espacios y todo dentro de % %
     """


# db = DbAnimeSearch()
# db.create_tab_animebysearch()
# db.insert_animebysearch()
# db.show_animebysearch()