import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ebaded740ce053782f687cdb94fb9544'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

BODY_POKEMON_CREATION = {
    "name": "generate",
    "photo_id": -1
}

RESPONSE_POKEMON_CREATION = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMON_CREATION)

print(RESPONSE_POKEMON_CREATION.text)

POKEMON_ID = RESPONSE_POKEMON_CREATION.json()['id']

BODY_CHANGE_NAME = {
    "pokemon_id": POKEMON_ID,
    "name": "Igor",
    "photo_id": -1
}

RESPONSE_CHANGE_NAME = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE_NAME)

print(RESPONSE_CHANGE_NAME.text)

BODY_POKEMON_CATCH = {"pokemon_id" : POKEMON_ID}

RESPONSE_POKEMON_CATCH = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEMON_CATCH)

print(RESPONSE_POKEMON_CATCH.text)