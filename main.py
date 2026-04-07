import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

data = response.json()

print(data["name"])
print(data["height"])