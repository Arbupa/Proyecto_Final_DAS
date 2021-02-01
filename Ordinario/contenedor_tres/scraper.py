import requests
import random
import time

class Scraper():
	def __init__(self) -> None:
		self.urlapi = 'https://api.jikan.moe/v3/'

		# Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujeron.
	def anime_by_name(self, anime_list:list) ->list:
		animes_to_search = anime_list
		lista = []
		for i in animes_to_search:
			response = requests.get(self.urlapi + 'search/anime?q=' + i)
			data = response.json()
			cont = 0

			while cont < 5:
				page_id = data['results'][cont].get('mal_id')
				title = str(data['results'][cont].get('title'))
				episodes = str(data['results'][cont].get('episodes'))
				image = str(data['results'][cont].get('image_url'))
				synopsis = str(data['results'][cont].get('synopsis'))
				tipo = str(data['results'][cont].get('type'))
				rated = str(data['results'][cont].get('rated'))
				score = str(data['results'][cont].get('score'))
				airing = str(data['results'][cont].get('airing'))
				members = str(data['results'][cont].get('members'))

				datos = {"page_id": page_id, "title": title, "episodes": episodes, "image_url": image, "synopsis": synopsis, "type": tipo, "rated": rated, "score": score, "airing": airing, "members": members}
				#print(datos)
				lista.append(datos)
				cont += 1

		#print(lista)
		return lista

		# Muestra información detallada sobre un anime en especifico gracias a su id
	def anime_by_id(self, id_anime:list) -> list:
		#Ahora guarda en forma de diccionario los primeros 50 id's de los animes dentro de una lista
		lista = []
		for cont in range (len(id_anime)):
			response = requests.get(self.urlapi + 'anime/' + str(cont+1))
			if response.status_code == 200:
				data = response.json()

				page_id = (data.get('mal_id'))
				image_url = (data.get('image_url'))
				title = str(data.get('title'))
				episodes = str(data.get('episodes'))
				status = str(data.get('status'))
				score = str(data.get('score'))
				rank = str(data.get('rank'))
				duration = str(data.get('duration'))
				synopsis = str(data.get('synopsis'))
				premiered = str(data.get('premiered'))
				broadcast = str(data.get('broadcast'))

				datos = {"page_id": page_id,"image_url": image_url, "title": title, "episodes": episodes, "status": status, "score": score, "rank": rank, "duration": duration, "synopsis": synopsis, "premiered": premiered, "broadcast": broadcast}

				lista.append(datos)
			if cont == 30:
				time.sleep(4)
		#print(len(lista))
		return lista

		# Muestra información de animes random que pertenezcan a ese genero (se guardan del 1 al 20)
	def anime_by_genre_id(self, id_list_search:list) -> list:
		lista = []
		contador = 1
		for i in range(len(id_list_search)):
			response = requests.get(self.urlapi + 'search/anime?genre=' + str(i+1))
			data = response.json()
			j = 0
			pos = 0
			if contador == 12:
				time.sleep(14)
				contador = 0
			while j < 5:
				#pos = random.randint(1, len(data['results']) - 1)
				id_genre = i+1
				page_id = data['results'][pos].get('mal_id')
				title = str(data['results'][pos].get('title'))
				image = str(data['results'][pos].get('image_url'))
				episodes = str(data['results'][pos].get('episodes'))
				airing = str(data['results'][pos].get('airing'))
				tipo = str(data['results'][pos].get('type'))
				start_date = str(data['results'][pos].get('start_date'))
				end_date = str(data['results'][pos].get('end_date'))
				members = str(data['results'][pos].get('members'))
				rated = str(data['results'][pos].get('rated'))
				#synopsis = str(data['results'][pos].get('synopsis'))

				datos = {"id_genre": id_genre, "page_id": page_id, "title": title, "image_url": image, "episodes": episodes, "airing": airing, "type": tipo, "start_date": start_date, "end_date": end_date, "members": members, "rated": rated}
				lista.append(datos)
				j += 1
				pos += 1
			contador +=1
		return lista

		# Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujo
	def manga_by_name(self, manga_list:list):
		mangas_to_search = manga_list
		lista = []

		for i in mangas_to_search:
			response = requests.get(self.urlapi + 'search/manga?q=' + i)
			data = response.json()
			cont = 0

			while cont < 5:
				page_id = data['results'][cont].get('mal_id')
				image = str(data['results'][cont].get('image_url'))
				title = str(data['results'][cont].get('title'))
				publishing = str(data['results'][cont].get('publishing'))
				synopsis = str(data['results'][cont].get('synopsis'))
				tipo = str(data['results'][cont].get('type'))
				chapters = str(data['results'][cont].get('chapters'))
				volumes = str(data['results'][cont].get('volumes'))
				start_date = str(data['results'][cont].get('start_date'))
				end_date = str(data['results'][cont].get('end_date'))

				datos = {"page_id": page_id, "image_url": image, "title": title, "publishing": publishing, "synopsis": synopsis, "type": tipo, "chapters": chapters, "volumes": volumes, "start_date": start_date, "end_date": end_date}
				lista.append(datos)
				cont += 1
		return lista

# resultados = Scraper()
# animes_to_search = ["shingeki no kyojin", "pokemon", "boku no hero", "code geass", "hunter x hunter", "shokugeki no souma"]
# print(resultados.anime_by_name(animes_to_search))
# time.sleep(4)

# id_anime = [num for num in range(1, 105)]
# print(resultados.anime_by_id(id_anime))
# time.sleep(12)

# mangas = ["kimetsu no yaiba", "berserk", "one piece", "dragon ball", "saint seiya"]
# print(resultados.manga_by_name(mangas))
# time.sleep(12)

# lista_ids = [num for num in range(1, 21)]
# print(resultados.anime_by_genre_id(lista_ids))
