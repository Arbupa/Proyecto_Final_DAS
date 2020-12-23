import mysql.connector
from mysql.connector import cursor

class DataBaseInteract():
#Creo el conexión string
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
                  page_id varchar(20), title varchar(150), episodes varchar(20), type varchar(20),
                  rated varchar(20), image_url varchar(200), score varchar(20), synopsis varchar(2000),
                  airing varchar(50), members varchar(20), PRIMARY KEY (id)
                  );"""

      if self.mycursor.execute(query_table):
          print("se creó la tabla")
      else:
          print("NO se creó la tabla")

    def insert_animebysearch(self):
        query = "INSERT INTO animebysearch (page_id, title, episodes, type, rated, image_url, score, synopsis, airing, members) VALUES ('20','Naruto','360','seinen','8.9','www.bla.com','8','ksjacnkjxsnckjasnckjas','2002','yo');"
        # query = f"INSERT INTO animebysearch VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('episodes')}','{i.get('type')}','{i.get('rated')}','{i.get('image_url')}','{i.get('score')}','{i.get('synopsis')}','{i.get('airing')}','{i.get('members')}');"
        self.mycursor.execute(query)
        self.mydb.commit()
        return "se inserto"

    def show_animebysearch(self):
        query = ("SELECT * FROM animebysearch;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print(row)

db = DataBaseInteract()
db.create_tab_animebysearch()
db.insert_animebysearch()
db.show_animebysearch()