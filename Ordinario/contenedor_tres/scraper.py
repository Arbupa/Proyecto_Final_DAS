import requests
import random
import time

urlapi = 'https://api.jikan.moe/v3/'


def animedetaillsname():
	#Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujo
	name = ["shingeki no kyojin", "death note", "boku no hero", "code geass"]
	lista = []
	for i in name:
		response = requests.get(urlapi + 'search/anime?q=' + i)
		data = response.json()
		cont = 0

		while cont < 5:
			id = data['results'][cont].get('mal_id')
			title = str(data['results'][cont].get('title'))
			episodes = str(data['results'][cont].get('episodes'))
			image = str(data['results'][cont].get('image_url'))
			synopsis = str(data['results'][cont].get('synopsis'))
			tipo = str(data['results'][cont].get('type'))
			rated = str(data['results'][cont].get('rated'))
			score = str(data['results'][cont].get('score'))
			airing = str(data['results'][cont].get('airing'))
			members = str(data['results'][cont].get('members'))

			datos = {"id": id, "title": title, "episodes": episodes, "image": image, "synopsis": synopsis, "tipo": tipo, "rated": rated, "score": score, "airing": airing, "members": members}
			#print(datos)
			lista.append(datos)
			cont += 1

	print(lista)
	return lista

def animedetaillsid():
	#Muestra información detallada sobre un anime en especifico gracias a su id
	#Ahora guarda en forma de diccionario los primeros 50 id's de los animes dentro de una lista
	lista = []
	for cont in range (1, 51):
		response = requests.get(urlapi + 'anime/' + str(cont))
		#print(response)
		data = response.json()

		id = (data.get('mal_id'))
		title = str(data.get('title'))
		episodes = str(data.get('episodes'))
		status = str(data.get('status'))
		score = str(data.get('score'))
		rank = str(data.get('rank'))
		duration = str(data.get('duration'))
		synopsis = str(data.get('synopsis'))
		premiered = str(data.get('premiered'))
		broadcast = str(data.get('broadcast'))

		datos = {"id": id, "title": title, "episodes": episodes, "status": status, "score": score, "rank": rank, "duration": duration, "synopsis": synopsis, "premiered": premiered, "broadcast": broadcast}

		lista.append(datos)
	print(lista)
	return lista

def animeforgenreid():
	#Muestra información de 10 animes random que pertenezcan a ese genero (se guardan del 1 al 15)
	lista = []
	contador = 1
	for i in range(1, 43):
		response = requests.get(urlapi + 'search/anime?genre=' + str(i))
		data = response.json()
		j = 0
		if contador == 15:
			time.sleep(17)
			contador = 0
		while j < 5:

			#x = random.randint(1, len(data['results']) - 1)

			id = data['results'][j].get('mal_id')
			title = str(data['results'][j].get('title'))
			image = str(data['results'][j].get('image_url'))
			episodes = str(data['results'][j].get('episodes'))
			airing = str(data['results'][j].get('airing'))
			tipo = str(data['results'][j].get('type'))
			start_date = str(data['results'][j].get('start_date'))
			end_date = str(data['results'][j].get('end_date'))
			members = str(data['results'][j].get('members'))
			rated = str(data['results'][j].get('rated'))

			datos = {"id": id, "title": title, "image": image, "episodes": episodes, "airing": airing, "tipo": tipo, "start_date": start_date, "end_date": end_date, "members": members, "rated": rated}
			print(datos)
			print(i)
			lista.append(datos)
			j += 1
		contador +=1
	return lista

def mangaforname():
	#Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujo
	name = ["kimetsu no yaiba", "pokemon", "berserk", "one piece"]
	lista = []

	for i in name:
		response = requests.get(urlapi + 'search/manga?q=' + i)
		data = response.json()
		cont = 0

		while cont < 5:
			id = data['results'][cont].get('mal_id')
			image = str(data['results'][cont].get('image_url'))
			title = str(data['results'][cont].get('title'))
			publishing = str(data['results'][cont].get('publishing'))
			synopsis = str(data['results'][cont].get('synopsis'))
			tipo = str(data['results'][cont].get('type'))
			chapters = str(data['results'][cont].get('chapters'))
			volumes = str(data['results'][cont].get('volumes'))
			start_date = str(data['results'][cont].get('start_date'))
			end_date = str(data['results'][cont].get('end_date'))

			datos = {"id": id, "image": image, "title": title, "publishing": publishing, "synopsis": synopsis, "tipo": tipo, "chapters": chapters, "volumes": volumes, "start_date": start_date, "end_date": end_date}
			lista.append(datos)
			cont += 1
	print(lista)
	return lista

#Para testear el funcionamiento
resultados1 = animedetaillsid()
time.sleep(6)
resultados2 = animedetaillsname()
time.sleep(16)
resultados3	= animeforgenreid()
time.sleep(12)
resultados4 = mangaforname()

#print(resultados1)
#print("-----------------")
#print(resultados2)
#print("-----------------")
#print(resultados3)
#print("-----------------")
#print(resultados4)