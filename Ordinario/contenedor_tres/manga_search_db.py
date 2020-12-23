import mysql.connector
from mysql.connector import cursor

class DataBaseInteract4():

    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="invitao",
                    password="secret123",
                    database="app_db"
                    )
  
        self.mycursor = self.mydb.cursor()

    def create_tab_mangabysearch(self):
      query_table = """CREATE TABLE mangabysearch ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  page_id varchar(20), image_url varchar(200),  title varchar(150), publishing varchar(50), type varchar(20),
                  chapters varchar(20), volumes varchar(20), synopsis varchar(2000),
                  start_date varchar(50), end_date varchar(20)
                  );"""

      if self.mycursor.execute(query_table):
          print("se creó la db")
      self.mycursor.execute("SHOW TABLES")
      for x in self.mycursor:
        print(x)

    def insert_mangabysearch(self):
    
    	  #inf = mangaforname()

    	  #for i in inf:
    		#query = f"INSERT INTO mangabysearch VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('publishing')}','{i.get('type')}','{i.get('chapters')}','{i.get('image_url')}','{i.get('volumes')}','{i.get('synopsis')}','{i.get('start_date')}','{i.get('end_date')}');"
        query = "INSERT INTO mangabysearch (page_id, image_url, title, publishing, type, chapters, volumes, synopsis, start_date, end_date) VALUES ('c','c','c','c','c','c','c','c','c','c');"
        self.mycursor.execute(query)
        self.mydb.commit()
        return "se inserto"

    def show_tab_mangabysearch(self):
        query = ("SELECT * FROM mangabysearch;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)

db=DataBaseInteract4()
#db.create_tab_mangabysearch()
db.insert_mangabysearch()
db.show_tab_mangabysearch()