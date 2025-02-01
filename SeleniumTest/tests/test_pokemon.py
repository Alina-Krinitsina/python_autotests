import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b3b47a08c2d7410262df5cbbbffc2dfa'
HEADER = {'Content-Tipe' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28622'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200


def test_name():
    response_get = requests.get(url= f'{URL}/trainers')
    assert response_get.json()["data"][8]["trainer_name"] == 'Леон'




