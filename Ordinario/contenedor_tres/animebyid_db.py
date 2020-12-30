import mysql.connector
from mysql.connector import cursor
from getpass import getpass


class DbAnimeById():
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
                  page_id Int, title varchar(150), episodes varchar(20), status varchar(75),
                  score varchar(20), rank varchar(20), duration varchar(50), synopsis varchar(3000),
                  premiered varchar(50), broadcast varchar(80)
                  );"""

      if self.mycursor.execute(query_table) == False:
          print("se creó la db")
      else:
          print("La tabla ya existe")
    #self.mycursor.execute("SHOW TABLES")
    #   for x in self.mycursor:
    #     print(x)

    def insert_animebyid(self, lista):
        print("La lista desde la db es:")
        print(lista)
        for i in lista:
            synopsis = i["synopsis"]
            synopsis = synopsis.replace("'", "")
            title = i["title"]
            title = title.replace("'", "")
            query = f"INSERT INTO animebyid (page_id, title, episodes, status, score, rank, duration, synopsis, premiered, broadcast) VALUES ('{i['page_id']}','{title}','{i['episodes']}','{i['status']}','{i['score']}','{i['rank']}','{i['duration']}','{synopsis}','{i['premiered']}','{i['broadcast']}');"
            self.mycursor.execute(query)
            self.mydb.commit()
        return "se insertaron"

    def show_tab_animebyid(self):
        query = ("SELECT * FROM animebyid;")
        self.mycursor.execute(query)
        for row in self.mycursor:
            print (row)


# if __name__ == "__main__":
#     print(insert_animebyid())
#     print(show_tab_animebyid())
#db = DbAnimeById()
#db.create_tab_animebyid()
#db.insert_animebyid()
#db.show_tab_animebyid()