import requests
import json

def get_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    return response.json()

data = []

for i in range(1, 51):  # primeiros 50 pokemons
    pokemon = get_pokemon(i)
    data.append(pokemon)

with open("data/raw/pokemons.json", "w") as f:
    json.dump(data, f)