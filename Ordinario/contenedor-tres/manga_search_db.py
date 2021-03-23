import mysql.connector
from mysql.connector import cursor

class DbManga():
    
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
                    page_id Int, image_url varchar(200),  title varchar(150), publishing varchar(50), type varchar(20),
                    chapters varchar(20), volumes varchar(20), synopsis varchar(2000),
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
        return "se insertaron"

    def show_tab_mangabysearch(self):
        query = ("SELECT * FROM mangabysearch;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)

#db=DbManga()
#db.create_tab_mangabysearch()
#db.insert_mangabysearch()
#db.show_tab_mangabysearch()