from flask import redirect, url_for, render_template
from flask.app import Flask
import mysql.connector
import requests


app = Flask(__name__)

@app.route("/")
def first():
    #return render_template("test.html")
    return render_template("index.html")
#El redirect se viene a esta ruta y consume la api
@app.route("/anime_search/<int:num>", methods = ['GET', 'POST'])
def search(num):
    r = requests.get(f'https://api.jikan.moe/v3/anime/{num}')
    data = r.json()
    return render_template("anime_search.html", data = data)

@app.route("/anime_busqueda<string:busqueda>", methods = ['GET'])
def search_by_id(busqeda):
    conn = conn_db
    query = "SELECT * FROM animebysearch WHERE"
    return render_template("anime_busqueda.html")

@app.route("/asdsa", methods = ['GET', 'POST'])
def testep():
    return render_template("anime_search.html")

@app.route("/agregar", methods = ['GET', 'POST'])
def ajustar():
    return render_template("anime_search.html")

def conn_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="invitao",
    password="secret123",
    database="app_db"
    )
    mycursor = mydb.cursor()
    return mycursor

if __name__ == "__main__":
    app.run(debug=True, port=4000)