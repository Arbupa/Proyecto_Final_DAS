import requests


r = requests.get(f'https://api.jikan.moe/v3/anime/20')
data = r.json()

print(data['image_url'])
for i in data:
    print(i)