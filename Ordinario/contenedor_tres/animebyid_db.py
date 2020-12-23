import mysql.connector
from mysql.connector import cursor
from getpass import getpass


class DataBaseInteract2():
#Creo el conexión string
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="invitao",
                    password="secret123",
                    database="app_db"
                    )
  
        self.mycursor = self.mydb.cursor()

    def create_tab_animebyid(self):
      query_table = """CREATE TABLE animebyid (id Int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  page_id varchar(20), title varchar(150), episodes varchar(20), status varchar(75),
                  score varchar(20), rank varchar(20), duration varchar(50), synopsis varchar(2000),
                  premiered varchar(50), broadcast varchar(80)
                  );"""

      if self.mycursor.execute(query_table):
          print("se creó la db")
      self.mycursor.execute("SHOW TABLES")
      for x in self.mycursor:
        print(x)

    def insert_animebyid(self):

      # for i in inf:
      
      #query = f"INSERT INTO animebyid (page_id, title, episodes, status, score, rank, duration, synopsis, premieredm, broadcast) VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('episodes')}','{i.get('status')}','{i.get('score')}','{i.get('rank')}','{i.get('duration')}','{i.get('synopsis')}','{i.get('premiered')}','{i.get('broadcast')}');"
      #no moverle tanto al insert
        query = "INSERT INTO animebyid (page_id, title, episodes, status, score, rank, duration, synopsis, premiered, broadcast) VALUES ('a','a','a','a','a','a','a','a','a','a');"
        self.mycursor.execute(query)
        self.mydb.commit()
        return "se inserto"

    def show_tab_animebyid(self):
        query = ("SELECT * FROM animebyid;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)


# if __name__ == "__main__":
#     print(insert_animebyid())
#     print(show_tab_animebyid())
db = DataBaseInteract2()
#db.create_tab_animebyid()
db.insert_animebyid()
db.show_tab_animebyid()