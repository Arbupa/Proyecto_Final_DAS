import mysql.connector
from mysql.connector import cursor

class DataBaseInteract3():

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
                  page_id varchar(20), title varchar(150),image_url varchar(200), episodes varchar(20), airing varchar(20),
                  type varchar(20), start_date varchar(50), end_date varchar(50),
                  members varchar(20), rated varchar(10)
                  );"""

      if self.mycursor.execute(query_table):
          print("se creó la db")
      self.mycursor.execute("SHOW TABLES")
      for x in self.mycursor:
        print(x)

    def insert_animebygenre(self):
      #for i in inf:
        #Usar este insert de abajo
        query = "INSERT INTO animebygenre (page_id, title, image_url, episodes, airing, type, start_date, end_date, members, rated) VALUES ('b','b','b','b','b','b','b','b','b','b');"
        #query = f"INSERT INTO animebygenre VALUES ('1','2','3','4','5','6','7','8','9','10');"
        self.mycursor.execute(query)
        self.mydb.commit()
        return "se inserto"

    def show_tab_animebygenre(self):
        query = ("SELECT * FROM animebygenre;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)

db = DataBaseInteract3()
#db.create_tab_animebygenre()
db.insert_animebygenre()
db.show_tab_animebygenre()
