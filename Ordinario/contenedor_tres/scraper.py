import requests
import random

urlapi = 'https://api.jikan.moe/v3/'


def animedetaillsname():
	#Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujo
	name = "one piece"

	response = requests.get(urlapi + 'search/anime?q=' + name)
	data = response.json()

	lista = []

	i = 0

	while i < 5:
		id = str(data['results'][i].get('mal_id'))
		title = str(data['results'][i].get('title'))
		episodes = str(data['results'][i].get('episodes'))
		image = str(data['results'][i].get('image_url'))
		synopsis = str(data['results'][i].get('synopsis'))
		tipo = str(data['results'][i].get('type'))
		rated = str(data['results'][i].get('rated'))
		score = str(data['results'][i].get('score'))
		airing = str(data['results'][i].get('airing'))
		members = str(data['results'][i].get('members'))
		
		datos = {"id": id, "title": title, "episodes": episodes, "image": image, "synopsis": synopsis, "tipo": tipo, "rated": rated, "score": score, "airing": airing, "members": members}
		#print(datos)
		lista.append(datos)

		i += 1
	
	return lista

def animedetaillsid():
	##Muestra información detallada sobre un anime en especifico gracias a su id
	identificador = "20"

	response = requests.get(urlapi + 'anime/' + identificador)
	print(response)
	data = response.json()

	lista = []

	id = str(data.get('mal_id'))
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
	print (lista)
	return lista

def animeforgenreid():
	#Muestra información de 10 animes random que pertenezcan a ese genero
	identificador = "27"

	response = requests.get(urlapi + 'search/anime?genre=' + identificador)
	data = response.json()

	lista = []

	i = 0

	while i < 10:

		x = random.randint(0, len(data['results']) - 1)

		id = str(data['results'][x].get('mal_id'))
		title = str(data['results'][x].get('title'))
		image = str(data['results'][x].get('image_url'))
		episodes = str(data['results'][x].get('episodes'))
		airing = str(data['results'][x].get('airing'))
		tipo = str(data['results'][x].get('type'))
		start_date = str(data['results'][x].get('start_date'))
		end_date = str(data['results'][x].get('end_date'))
		members = str(data['results'][x].get('members'))
		rated = str(data['results'][x].get('rated'))

		datos = {"id": id, "title": title, "image": image, "episodes": episodes, "airing": airing, "tipo": tipo, "start_date": start_date, "end_date": end_date, "members": members, "rated": rated}
		print(datos)
		lista.append(datos)

		i += 1
	
	return lista

def mangaforname():
	#Muestra la información de los primeros 5 resultados más relacionados encontrados por el nombre que se introdujo
	name = "kimetsu no yaiba"

	response = requests.get(urlapi + 'search/manga?q=' + name)
	data = response.json()

	lista = []

	i = 0

	while i < 5:
		id = str(data['results'][i].get('mal_id'))
		image = str(data['results'][i].get('image_url'))
		title = str(data['results'][i].get('title'))
		publishing = str(data['results'][i].get('publishing'))
		synopsis = str(data['results'][i].get('synopsis'))
		tipo = str(data['results'][i].get('type'))
		chapters = str(data['results'][i].get('chapters'))
		volumes = str(data['results'][i].get('volumes'))
		start_date = str(data['results'][i].get('start_date'))
		end_date = str(data['results'][i].get('end_date'))
		
		datos = {"id": id, "image": image, "title": title, "publishing": publishing, "synopsis": synopsis, "tipo": tipo, "chapters": chapters, "volumes": volumes, "start_date": start_date, "end_date": end_date}
		
		lista.append(datos)

		i += 1
	
	return lista

#Para testear el funcionamiento
#resultados1 = animedetaillsid()
#resultados2 = animedetaillsname()
resultados3	= animeforgenreid()
#resultados4 = mangaforname()

#print(resultados1)
#print("-----------------")
#print(resultados2)
#print("-----------------")
#print(resultados3)
#print("-----------------")
#print(resultados4)