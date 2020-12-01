import mysql.connector
from mysql.connector import cursor
from scraper import animeforgenreid

mydb = mysql.connector.connect(
  host="localhost",
  user="invitao",
  password="secret123",
  database="app_db"
)

mycursor = mydb.cursor()

def create_tab_animebygenre():
  query_table = """CREATE TABLE animebygenre ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
              page_id varchar(20), title varchar(150), episodes varchar(20), airing varchar(20),
              type varchar(20), image_url varchar(200), start_date varchar(50), end_date varchar(50),
              members varchar(20), rated varchar(10)
              );"""

  if mycursor.execute(query_table):
      print("se creó la db")
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
    print(x)

def insert_animebygenre():
  inf = animeforgenreid()
    
  for i in inf:
    #query = f"INSERT INTO animebygenre VALUES ('{i['id']}','{i['title']}','{i['episodes']}','{i['airing']}','{i['tipo']}','{i['image']}','{i['start_date']}','{i['end_date']}','{i['members']}','{i['rated']}');"
    query = f"INSERT INTO animebygenre VALUES ('1','2','3','4','5','6','7','8','9','10');"
    mycursor.execute(query)
  return "se inserto"

def show_tab_animebygenre():
    query = ("SELECT * FROM animebygenre;")
    mycursor.execute(query)
    for row in mycursor:
        print (row)

create_tab_animebygenre()
insert_animebygenre()
show_tab_animebygenre()