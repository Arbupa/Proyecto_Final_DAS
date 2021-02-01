from flask import redirect, url_for, render_template, jsonify, request
from flask.app import Flask
import requests
#import sys
#sys.path.insert(0, '../contenedor_cuatro')
#from test import *
from basealchemy import *
from models import *

app = Flask(__name__)

class UniqueVar():
    def __init__(self, last_search) -> None:
        self.last_search = last_search
        
global_search = UniqueVar("")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/anime_search/<string:search>", methods = ['GET'])
def get_anime_search(search):
    #quitar lo de global, para redireccionar después de un cambio
    global_search.last_search = search
    query_response = session.query(AnimeBySearch).filter(AnimeBySearch.title.like(f"%{search}%"))
    last_search = ""
    last_search = search
    return render_template("anime_search.html", query_response = query_response, global_search = global_search)

@app.route("/anime_search/delete/<int:id>", methods = ["DELETE"])
def delete_anime_search(id):
    #form = ""
    
    #print(f"La ultima busqueda fue: {last_search}")
    if request.method == "DELETE":
        query_response = session.query(AnimeBySearch).filter(AnimeBySearch.id == id).delete()
        session.commit()
        query_return = session.query(AnimeBySearch).filter(AnimeBySearch.title.like(f"%{global_search.last_search}%"))
        return render_template("anime_search.html", query_return = query_return)
    else:
        return "ID not found"


@app.route("/manga_search/<string:search>", methods = ["GET"])
def get_manga_search(search):
    query_response = session.query(MangaSearch).filter(MangaSearch.title.like(f"%{search}%"))
    return render_template("manga_search.html", query_response = query_response)

@app.route("/manga_search/<int:id>", methods = ["DELETE"])
def delete_manga_search(id):
    if request.method == "DELETE":
        query_response = session.query(MangaSearch).filter(MangaSearch.id == id).delete()
        session.commit()
    else:
        "Error: something gone wrong."
    # checar bien cómo mandarle la info después de actualizar un dato
    return render_template("manga_search.html")


# @app.route("/anime_search/<string:busqueda>", methods = ['POST'])
# def update_anime_search(busqueda):
#     return render_template("anime_search.html", busqueda = busqueda)

# @app.route("/anime_search/<id:id>", methods = ['PUT'])
# def update_anime_search(id):
#     return render_template("anime_search.html", id = id)

# @app.route("/anime_search/<int:id>", methods = ['DELETE'])
# def update_anime_search(id):
#     return render_template("anime_search.html", id = id)
@app.route("/anime_byid/<int:id>", methods = ['GET'])
def show_anime_by_id(id: int):
        query_response = session.query(AnimeById).get(id)
        if query_response == None:
            return print("ID not found")
        else:
            print(query_response.title, query_response.image_url)
            return render_template("anime_by_id.html", query_response = query_response)

@app.route("/anime_byid/<int:id>", methods = ["DELETE"])
def delete_anime_by_id(id):
    if request.method == "DELETE":
        query_response = session.query(AnimeById).filter(AnimeById.id == id).delete()
        session.commit()
        return "this is working"
    else:
        return "Error: something gone wrong."

@app.route("/anime_byid/edit/<int:id>", methods = ['POST'])
def edit_genre_by_id(id: int):
        query_response = session.query(AnimeById).get(id)
        if query_response == None:
            return print("ID not found")
        else:
            print(query_response.title, query_response.synopsis)
            return render_template("anime_by_id.html", query_response = query_response)

# @app.errorhandler(404)
# def page_not_found(error):
# 	return render_template("error.html",error="Página no encontrada..."), 404
@app.route("/genre_byid/<int:id>", methods = ['GET'])
def show_genre_by_id(id: int):
        query_response = session.query(AnimeByGenre).filter(AnimeByGenre.id_genre == id)
        if query_response == None:
            return print("ID not found")
        else:
            for i in query_response:
                print(i.title, i.image_url)
            return render_template("genre_anime.html", query_response = query_response)

@app.route("/genre_byid/<int:id>", methods = ["DELETE"])
def delete_genre_by_id(id):
    if request.method == "DELETE":
        query_response = session.query(AnimeByGenre).filter(AnimeByGenre.id == id).delete()
        session.commit()
        return "this is working"
    else:
        return "Error: something gone wrong."

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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
#print(var)