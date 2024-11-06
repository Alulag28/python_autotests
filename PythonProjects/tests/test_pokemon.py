import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ebaded740ce053782f687cdb94fb9544'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '7067'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id_in_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][5]["trainer_id"] == '7067'