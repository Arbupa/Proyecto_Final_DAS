import mysql.connector
from mysql.connector import cursor
from scraper import animedetaillsname

mydb = mysql.connector.connect(
  host="localhost",
  user="invitao",
  password="secret123",
  database="app_db"
)

mycursor = mydb.cursor()

def create_tab_animebysearch():
  query_table = """CREATE TABLE animebysearch ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
              page_id varchar(20), title varchar(150), episodes varchar(20), type varchar(20),
              rated varchar(20), image_url varchar(200), score varchar(20), synopsis varchar(2000),
              airing varchar(50), members varchar(20)
              );"""

  if mycursor.execute(query_table):
      print("se creó la db")
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
    print(x)

def insert_animebysearch():
    
    inf = animedetaillsname()
    
    for i in inf:
      query = f"INSERT INTO animebysearch VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('episodes')}','{i.get('type')}','{i.get('rated')}','{i.get('image_url')}','{i.get('score')}','{i.get('synopsis')}','{i.get('airing')}','{i.get('members')}');"
      mycursor.execute(query)
    
    return "se inserto"

def show_animebysearch():
    query = ("SELECT * FROM animebysearch;")
    mycursor.execute(query)
    for row in mycursor:
        print (row)

create_tab_animebysearch()