import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b3b47a08c2d7410262df5cbbbffc2dfa'
HEADER = {'Content-Tipe' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}


body_change = {
    "pokemon_id": "209892",
    "name": "Vova",
    "photo_id": 2
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_pokeball.text)