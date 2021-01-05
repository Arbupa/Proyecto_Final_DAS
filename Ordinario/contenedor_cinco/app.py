from flask import redirect, url_for, render_template
from flask.app import Flask
import mysql.connector
import requests
# import sys
# sys.path.insert(0, '../contenedor_cuatro')
# import apirest

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/anime_search/<string:busqueda>", methods = ['GET'])
def get_anime_search(busqueda):
    return render_template("anime_search.html", busqueda = busqueda)

@app.route("/anime_search/<string:busqueda>", methods = ['POST'])
def update_anime_search(busqueda):
    return render_template("anime_search.html", busqueda = busqueda)

@app.route("/anime_search/<id:id>", methods = ['PUT'])
def update_anime_search(id):
    return render_template("anime_search.html", id = id)

@app.route("/anime_search/<int:id>", methods = ['DELETE'])
def update_anime_search(id):
    return render_template("anime_search.html", id = id)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404


# @app.route("/anime_busqueda<string:busqueda>", methods = ['GET'])
# def search_by_id(busqeda):
#     conn = conn_db
#     query = "SELECT * FROM animebysearch WHERE title = {busqueda}"
#     return render_template("anime_busqueda.html")

# @app.route("/asdsa", methods = ['GET', 'POST'])
# def testep():
#     return render_template("anime_search.html")

# @app.route("/agregar", methods = ['GET', 'POST'])
# def ajustar():
#     return render_template("anime_search.html")

# def conn_db():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="invitao",
#     password="secret123",
#     database="app_db"
#     )
#     mycursor = mydb.cursor()
#     return mycursor

if __name__ == "__main__":
    app.run(debug=True, port=5000)