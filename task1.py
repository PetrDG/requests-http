import requests
from pprint import pprint

name = ["Hulk", "Captain America", "Thanos"]
hero = {}
i = 0
name_hero = None

for w in name:
    url = "https://superheroapi.com/api/2619421814940190/search/" + w
    response = requests.get(url=url)
    result = response.json()['results']
    if 'powerstats' in result[0]:
        hero[w] = result[0]['powerstats']['intelligence']
        for key, value in hero.items():
            if int(value) > i:
                name_hero = key
print(name_hero)