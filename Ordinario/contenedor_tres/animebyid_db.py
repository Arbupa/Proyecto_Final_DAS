import mysql.connector
from mysql.connector import cursor
from getpass import getpass
from scraper import animedetaillsid

mydb = mysql.connector.connect(
  host="localhost",
  user="invitao",
  password="secret123",
  database="app_db"
)

mycursor = mydb.cursor()
def create_tab_animebyid():
  query_table = """CREATE TABLE animebyid (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
              page_id varchar(20), title varchar(150), episodes varchar(20), status varchar(75),
              score varchar(20), rank varchar(20), duration varchar(50), synopsis varchar(2000),
              premiered varchar(50), broadcast varchar(80)
              );"""

  if mycursor.execute(query_table):
      print("se creó la db")
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
    print(x)

def insert_animebyid():
  inf = animedetaillsid()
  for i in inf:
    query = f"INSERT INTO animebyid VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('episodes')}','{i.get('status')}','{i.get('score')}','{i.get('rank')}','{i.get('duration')}','{i.get('synopsis')}','{i.get('premiered')}','{i.get('broadcast')}');"
    mycursor.execute(query)
  return "se inserto"

def show_tab_animebyid():
    query = ("SELECT * FROM animebyid;")
    mycursor.execute(query)
    for row in mycursor:
        print (row)


# if __name__ == "__main__":
#     print(insert_animebyid())
#     print(show_tab_animebyid())
create_tab_animebyid()