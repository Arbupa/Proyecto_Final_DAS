import mysql.connector
from mysql.connector import cursor
from scraper import mangaforname

mydb = mysql.connector.connect(
  host="localhost",
  user="invitao",
  password="secret123",
  database="app_db"
)

mycursor = mydb.cursor()

def create_tab_mangabysearch():
  query_table = """CREATE TABLE mangabysearch ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
              page_id varchar(20), title varchar(150), publishing varchar(50), type varchar(20),
              chapters varchar(20), image_url varchar(200), volumes varchar(20), synopsis varchar(2000),
              start_date varchar(50), end_date varchar(20)
              );"""

  if mycursor.execute(query_table):
      print("se creó la db")
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
    print(x)

def insert_mangabysearch():

	inf = mangaforname()
	
	for i in inf:
		query = f"INSERT INTO mangabysearch VALUES ('{i.get('mal_id')}','{i.get('title')}','{i.get('publishing')}','{i.get('type')}','{i.get('chapters')}','{i.get('image_url')}','{i.get('volumes')}','{i.get('synopsis')}','{i.get('start_date')}','{i.get('end_date')}');"
		mycursor.execute(query)
    
	return "se inserto"

def show_tab_mangabysearch():
    query = ("SELECT * FROM mangabysearch;")
    mycursor.execute(query)
    for row in mycursor:
        print (row)

create_tab_mangabysearch()